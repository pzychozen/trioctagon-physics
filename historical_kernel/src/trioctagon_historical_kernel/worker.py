"""Fixed isolated worker, gated by the parent's resource Job before computation."""
import argparse
import base64
import json
import math
import os
from pathlib import Path
import sys
import time


def event(**value):
    print(json.dumps(value,separators=(",", ":")),flush=True)


def main():
    p=argparse.ArgumentParser()
    for name in ("admission","pin","candidate","destination","attempt"):p.add_argument("--"+name,required=True)
    p.add_argument("--started",type=int,required=True)
    args=p.parse_args()
    if not sys.flags.isolated or not sys.flags.dont_write_bytecode or sys.prefix==sys.base_prefix:
        raise RuntimeError("isolated installed worker is required")
    # No scientific import or request processing before the resource-job handshake.
    event(kind="ready",pid=os.getpid())
    if sys.stdin.buffer.readline(4)!=b"GO\n":
        return 2
    stage="CONTRACT";progress=0
    try:
        from .admission import Admission
        from .installation import verify_inventory,verify_numeric_environment,verify_runtime_closure
        from .resources import peak_memory
        from .numerics import NumericalFailure
        from .provider import evaluate
        from .artifacts import complete_claim
        from trioctagon_historical_protocol.requests import Request
        from trioctagon_historical_protocol.codec import ParseLimits
        admission=Admission.load_pinned(args.admission,args.pin)
        a=admission.to_dict();limits=a["resource"]["limits"]
        startup_us=(time.perf_counter_ns()-args.started)//1000
        stage="REQUEST"
        line=sys.stdin.buffer.readline(2*limits["input_bytes"]+2)
        raw=base64.b64decode(line,validate=False)
        request=Request.from_bytes(raw,ParseLimits(limits["input_bytes"],limits["json_depth"]))
        stage="CONTRACT";admission.validate_request(request);verify_numeric_environment();verify_runtime_closure()
        def check(completed=None):
            nonlocal progress
            elapsed=(time.perf_counter_ns()-args.started)/1000000
            if elapsed>limits["wall_milliseconds"] or peak_memory()>limits["memory_bytes"]:
                raise MemoryError("worker resource budget exhausted")
            if completed is not None and completed!=progress:
                progress=completed;event(kind="progress",updates_completed=progress)
        stage="RESOURCE";check()
        before=[]
        scan_started=time.perf_counter_ns()
        for inv in a["installed"]:
            check();actual=verify_inventory(inv)
            if inv["id"]=="trioctagon-historical-kernel":before=actual["members"]
        scan_ns=time.perf_counter_ns()-scan_started
        stage="COMPUTATION";event(kind="stage",stage=stage)
        payload=evaluate(request,admission,_control=check)
        stage="RESULT_BINDING";check();payload.validate_request(request);verify_numeric_environment();verify_runtime_closure()
        after=[]
        scan_started=time.perf_counter_ns()
        for inv in a["installed"]:
            check();actual=verify_inventory(inv)
            if inv["id"]=="trioctagon-historical-kernel":after=actual["members"]
        scan_ns+=time.perf_counter_ns()-scan_started
        serialize_started=time.perf_counter_ns()
        record=complete_claim(request,payload,admission,args.attempt,raw,before,after,
            math.ceil((time.perf_counter_ns()-args.started)/1000000),peak_memory())
        encoded=record.to_bytes();check()
        # Full serialization and binding have occurred. Take another actual local
        # observation before the final seal; the parent enforces the entire path.
        record=complete_claim(request,payload,admission,args.attempt,raw,before,after,
            math.ceil((time.perf_counter_ns()-args.started)/1000000),peak_memory())
        encoded=record.to_bytes();check()
        if len(encoded)>limits["output_bytes"]:
            raise MemoryError("aggregate output limit")
        stage="PERSISTENCE"
        with Path(args.candidate).open("xb") as stream:
            stream.write(encoded);stream.flush();os.fsync(stream.fileno())
        check()
        event(kind="candidate",bytes=len(encoded),updates_completed=progress,
            startup_microseconds=startup_us,scan_microseconds=scan_ns//1000,
            serialization_microseconds=(time.perf_counter_ns()-serialize_started)//1000)
        if sys.stdin.buffer.readline(9)!=b"PUBLISH\n":
            return 2
        check()
        # Same-volume atomic creation; never replace an existing destination.
        # Parent supervises this call and rolls back our own link on timeout.
        os.link(args.candidate,args.destination)
        check()
        event(kind="published")
        return 0
    except Exception as exc:
        category="RESOURCE_LIMIT" if isinstance(exc,MemoryError) else "PROVIDER_FAILURE"
        if isinstance(exc,FloatingPointError):category="NUMERICAL_DOMAIN_FAILURE"
        if hasattr(exc,"category"):
            category=exc.category
            if category in ("INVALID_SCHEMA","INVALID_CODEC"):
                category="MALFORMED_REQUEST" if stage=="REQUEST" else "RESULT_BINDING_FAILURE"
        elif isinstance(exc,ValueError) and stage=="CONTRACT":category="PROVIDER_IDENTITY_MISMATCH"
        if stage=="PERSISTENCE" and isinstance(exc,OSError):category="PERSISTENCE_FAILURE"
        event(kind="failure",category=category,stage=stage,updates_completed=progress)
        return 1

if __name__=="__main__":
    raise SystemExit(main())

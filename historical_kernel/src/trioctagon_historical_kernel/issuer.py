"""One local unattested lane. A pinned external admission is mandatory; B2 remains unavailable."""
import base64
import json
import os
from pathlib import Path
import queue
import subprocess
import sys
import tempfile
import threading
import time
import uuid
from trioctagon_historical_protocol.requests import Request
from trioctagon_historical_protocol.records import DerivedRecord
from trioctagon_historical_protocol.codec import ParseLimits
from trioctagon_historical_protocol.errors import CATEGORIES
from .admission import Admission
from .artifacts import receipt
from .resources import ProcessBudget

_LANE=threading.Lock()


def _publish(process):
    # Only authorize after the parent has validated the complete staged record.
    # The actual filesystem operation remains inside the supervised worker.
    process.stdin.write(b"PUBLISH\n");process.stdin.flush();process.stdin.close()


class LocalIssuer:
    def __init__(self, admission_path, admission_sha256):
        self.path=Path(admission_path).resolve()
        self.pin=admission_sha256
        self.admission=Admission.load_pinned(self.path,self.pin)

    def issue(self, raw, destination, *, cancellation=None):
        if type(raw) is not bytes:
            raise TypeError("exact submitted bytes required")
        if cancellation is not None and not isinstance(cancellation,threading.Event):
            raise TypeError("local threading.Event cancellation required")
        attempt=uuid.uuid4().hex
        started=time.perf_counter_ns()
        limits=self.admission.to_dict()["resource"]["limits"]
        request=None;progress=0;stage="REQUEST";checks=None;staging="NOT_CREATED"
        def failed(category):
            return receipt(raw,request,attempt,category,stage,progress,limits["diagnostic_bytes"],checks=checks,staging=staging)
        if not _LANE.acquire(blocking=False):
            return failed("RESOURCE_LIMIT")
        try:
            parsed=Request.from_bytes(raw,ParseLimits(limits["input_bytes"],limits["json_depth"]))
            stage="CONTRACT"
            self.admission.validate_request(parsed)
            request=parsed
            if cancellation is not None and cancellation.is_set():
                stage="CANCELLATION";return failed("CANCELLED")
            destination=Path(destination).resolve()
            stage="PERSISTENCE"
            destination.parent.mkdir(parents=True,exist_ok=True)
            with tempfile.TemporaryDirectory(prefix=".historical-stage-",dir=destination.parent) as temp:
                candidate=Path(temp)/"candidate.json"
                staging="DISCARDED"
                command=[sys.executable,"-I","-B","-m","trioctagon_historical_kernel.worker",
                    "--admission",str(self.path),"--pin",self.pin,"--candidate",str(candidate),"--destination",str(destination),
                    "--attempt",attempt,"--started",str(started)]
                events=queue.Queue(maxsize=8)
                stop_reader=threading.Event()
                stage="RESOURCE"
                env=dict(os.environ,PYTHONDONTWRITEBYTECODE="1",PYTHONUTF8="1")
                env.pop("PYTHONPATH",None);env.pop("PYTHONHOME",None)
                with subprocess.Popen(command,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.DEVNULL,
                    cwd=temp,env=env,creationflags=subprocess.CREATE_NO_WINDOW) as process:
                    budget=None;completed=False;thread=None
                    try:
                        budget=ProcessBudget(int(process._handle),limits["memory_bytes"])
                        def send_event(event):
                            while not stop_reader.is_set():
                                try:
                                    events.put(event,timeout=.05)
                                    return
                                except queue.Full:
                                    continue
                        def reader():
                            try:
                                while True:
                                    line=process.stdout.readline(65537)
                                    if not line:break
                                    if len(line)>65536:raise ValueError("oversized worker event")
                                    send_event(json.loads(line))
                            except Exception:
                                send_event(dict(kind="failure",category="PROVIDER_FAILURE",stage="COMPUTATION",updates_completed=0))
                            finally:send_event(dict(kind="eof"))
                        thread=threading.Thread(target=reader,daemon=True);thread.start()
                        result=None;published=False
                        while True:
                            elapsed=(time.perf_counter_ns()-started)/1000000
                            if cancellation is not None and cancellation.is_set():
                                stage="CANCELLATION";process.kill();return failed("CANCELLED")
                            if elapsed>limits["wall_milliseconds"] or budget.exceeded(limits["memory_bytes"]):
                                process.kill();return failed("RESOURCE_LIMIT")
                            try:event=events.get(timeout=.01)
                            except queue.Empty:continue
                            kind=event.get("kind")
                            if kind=="ready":
                                budget.attach_worker(event.get("pid"))
                                if budget.exceeded(limits["memory_bytes"]):
                                    process.kill();return failed("RESOURCE_LIMIT")
                                process.stdin.write(b"GO\n"+base64.b64encode(raw)+b"\n");process.stdin.flush()
                            elif kind=="stage":stage="COMPUTATION"
                            elif kind=="progress":
                                n=event.get("updates_completed")
                                if type(n) is not int or not progress<=n<=request.to_dict()["body"]["arguments"].get("updates",0):
                                    process.kill();return failed("PROVIDER_FAILURE")
                                progress=n
                            elif kind=="failure":
                                category=event.get("category")
                                stage=event.get("stage") if event.get("stage") in ("REQUEST","CONTRACT","INPUT","RESOURCE","COMPUTATION","RESULT_BINDING","PERSISTENCE") else "COMPUTATION"
                                return failed(category if category in CATEGORIES else "PROVIDER_FAILURE")
                            elif kind=="candidate":
                                if result is not None:return failed("PROVIDER_FAILURE")
                                stage="RESULT_BINDING"
                                with candidate.open("rb") as stream:encoded=stream.read(limits["output_bytes"]+1)
                                result=DerivedRecord.from_bytes(encoded,ParseLimits(limits["output_bytes"],limits["json_depth"]))
                                if result.to_dict()["request"]!=request.to_dict() or result.to_dict()["completion"]["attempt_id"]!=attempt:
                                    return failed("RESULT_BINDING_FAILURE")
                                checks=result.to_dict()["execution_evidence"]["checks"]
                                stage="PERSISTENCE"
                                if cancellation is not None and cancellation.is_set():
                                    stage="CANCELLATION";return failed("CANCELLED")
                                if (time.perf_counter_ns()-started)/1000000>limits["wall_milliseconds"]:
                                    return failed("RESOURCE_LIMIT")
                                _publish(process)
                            elif kind=="published":
                                if result is None:return failed("PROVIDER_FAILURE")
                                published=True
                            elif kind=="eof":break
                            else:process.kill();return failed("PROVIDER_FAILURE")
                        process.wait(timeout=max(.01,(limits["wall_milliseconds"]-elapsed)/1000))
                        if process.returncode or not published:
                            return failed("RESOURCE_LIMIT" if budget.exceeded(limits["memory_bytes"]) else "PROVIDER_FAILURE")
                        completed=True
                        return result
                    finally:
                        stop_reader.set()
                        if budget is not None:budget.close()
                        if process.poll() is None:process.kill()
                        process.wait(timeout=5)
                        if thread is not None:thread.join(timeout=1)
                        # A timeout can occur after link creation but before the
                        # worker confirms it. Remove only this attempt's own link.
                        if not completed and candidate.exists() and destination.exists() and os.path.samefile(candidate,destination):
                            destination.unlink()
        except Exception as exc:
            category=getattr(exc,"category",None)
            if isinstance(exc,(MemoryError,subprocess.TimeoutExpired)):
                category="RESOURCE_LIMIT"
            if category not in CATEGORIES:
                category="MALFORMED_REQUEST" if stage=="REQUEST" else "PROVIDER_IDENTITY_MISMATCH" if stage=="CONTRACT" else "PERSISTENCE_FAILURE" if stage=="PERSISTENCE" else "RESULT_BINDING_FAILURE"
            if category=="RESOURCE_LIMIT" and stage in ("CONTRACT","REQUEST"):
                stage="RESOURCE"
            return failed(category)
        finally:
            _LANE.release()

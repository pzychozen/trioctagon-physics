"""Supplement A only: independent exact expectations, then covering.py parity.

Run with conda torment Python -B. Output and scratch must be external.
Universal proofs are in the companion packet; bounded audits are FINITE_AUDIT.
No paper audit or tests are launched by this checker.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import subprocess
import sys
import tempfile

EXPECTED_HEAD = "34c21830e7e7c4b5f4a5a940d084c37feaf1f82c"
DEFAULT_REPO = Path(r"C:\TORMENT\TRIOCTAGON_new\trioctagon-physics")
REPORTS = Path(r"C:\Users\Notandi\.codex\reports")
PRIOR_REVIEW = [
    "TRIOCTAGON_CURRENT_KERNEL_MATHEMATICAL_COMPLETENESS_REVIEW_v0.1.md",
    "TRIOCTAGON_CURRENT_KERNEL_ATLAS_CROSSWALK_v0.1.json",
    "TRIOCTAGON_CURRENT_KERNEL_COMPLETENESS_CHECK.py",
    "TRIOCTAGON_CURRENT_KERNEL_COMPLETENESS_RESULTS.json",
]
SOURCE_RELS = [
    "kernel_physics/covering.py",
    "kernel_physics/tests/test_covering.py",
    "kernel_physics/K0_KERNEL_DEFINITION_LEDGER_v0.1.md",
    "papers/PAPER_A/publication/paper_A_publication.md",
    "papers/PAPER_A/PAPER_A_CYCLE_COVERING_DYNAMICS_DRAFT_v0.5.1.md",
    "papers/PAPER_A/PAPER_A_PROOF_AUDIT_v0.3.md",
    "research_files/verification/paperA/paperA_proof_audit_v0_2.py",
    "research/mathematical_atlas/entry_02_cycle_covering/"
    "TRIOCTAGON_ATLAS_02_3_TO_12_COVERING_SOURCE_PACKET_v0.1.md",
]


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--repo", type=Path, default=DEFAULT_REPO)
    ap.add_argument("--output", type=Path, required=True)
    ap.add_argument("--scratch", type=Path, required=True)
    ap.add_argument("--integrity-receipt", type=Path)
    ap.add_argument("--test-receipt", type=Path)
    ap.add_argument("--packaging-receipt", type=Path)
    ap.add_argument("--fingerprint-before", type=Path,
                    help="With the next two arguments, create a fresh external integrity receipt.")
    ap.add_argument("--external-before", type=Path)
    ap.add_argument("--git-before", type=Path)
    args = ap.parse_args()
    if not sys.dont_write_bytecode:
        ap.error("Run with -B (or PYTHONDONTWRITEBYTECODE=1).")
    repo, output, scratch = (p.resolve() for p in
                             (args.repo, args.output, args.scratch))
    protected = [repo, Path(r"C:\TORMENT").resolve()]
    for label, path in (("output", output), ("scratch", scratch)):
        if any(path == root or path.is_relative_to(root) for root in protected):
            ap.error(f"{label} must be external to protected trees")
    if output.exists():
        ap.error("output already exists; no overwrite")
    generate_integrity = any((args.fingerprint_before,args.external_before,args.git_before))
    if generate_integrity:
        if not all((args.fingerprint_before,args.external_before,args.git_before,args.integrity_receipt)):
            ap.error("integrity generation needs all three before manifests and --integrity-receipt")
        for path in (args.integrity_receipt.resolve(),
                     args.integrity_receipt.resolve().with_suffix(".after.json")):
            if path.exists() or any(path == root or path.is_relative_to(root) for root in protected):
                ap.error("new integrity receipt/after manifest must be unused external paths")
    if output.name in PRIOR_REVIEW or output.name.startswith("TRIOCTAGON_ATLAS_"):
        ap.error("prior Atlas/review output names are protected")
    source = repo / "kernel_physics/covering.py"
    if not source.is_file():
        ap.error("repo must contain kernel_physics/covering.py")
    scratch.mkdir(parents=True, exist_ok=True)
    run_dir = Path(tempfile.mkdtemp(prefix="supplement_a_", dir=scratch))
    for key in ("TMP", "TEMP", "TMPDIR", "MPLCONFIGDIR", "PYTHONPYCACHEPREFIX"):
        os.environ[key] = str(run_dir)
    tempfile.tempdir = str(run_dir)
    # The source file and package have NOT been imported at this point.
    import sympy as sp

    rows = []

    def check(group, name, ok, kind="EXACT_EXAMPLE", **detail):
        rows.append(dict(group=group, name=name, kind=kind,
                         passed=bool(ok), detail=detail))

    def matrix_json(a):
        return [[str(a[i, j]) for j in range(a.cols)] for i in range(a.rows)]

    def difference(m):
        # Independent construction: forward incidence difference, not the
        # production loop adding two neighbours.
        shift = sp.eye(m)[:, list(range(1, m)) + [0]].T
        return shift - sp.eye(m)

    def lap(m):
        b = difference(m)
        return -b.H * b

    def pull(m, d):
        # Vertically stack full identity blocks and an initial partial block.
        a, b = divmod(m, d)
        blocks = [sp.eye(d)] * a
        if b:
            blocks.append(sp.eye(d)[:b, :])
        return sp.Matrix.vstack(*blocks)

    def counts(m, d):
        a, b = divmod(m, d)
        return [a + int(r < b) for r in range(d)]

    def in_image(a, m, d):
        # A column belongs to im(P) iff its entries on each residue fibre agree.
        return all(a[n, :] == a[n % d, :] for n in range(m))

    def throws_value_error(fn):
        try:
            fn()
        except ValueError:
            return True
        return False

    bound = 12
    laps = {m: lap(m) for m in range(1, bound + 1)}
    pulls = {(m, d): pull(m, d) for m in laps for d in laps}
    q_expected = {(m, d): p / sp.sqrt(m // d)
                  for (m, d), p in pulls.items() if m % d == 0}
    for m, expected in {
        1: [[0]], 2: [[-2, 2], [2, -2]],
        3: [[-2, 1, 1], [1, -2, 1], [1, 1, -2]],
        4: [[-2, 1, 0, 1], [1, -2, 1, 0],
            [0, 1, -2, 1], [1, 0, 1, -2]],
    }.items():
        check("EXACT_CYCLE_LAPLACIAN", f"matrix_M{m}",
              laps[m] == sp.Matrix(expected), matrix=matrix_json(laps[m]))
    check("EXACT_CYCLE_LAPLACIAN", "degenerate_spectra",
          laps[1].eigenvals() == {0: 1}
          and laps[2].eigenvals() == {0: 1, -4: 1})
    cycle_bad = []
    for m, a in laps.items():
        z = sp.Matrix(sp.symbols(f"x0:{m}", complex=True))
        b = difference(m)
        ok = (a == a.H and a * sp.ones(m, 1) == sp.zeros(m, 1)
              and m - a.rank() == 1
              and sp.expand((z.H*a*z + (b*z).H*(b*z))[0]) == 0)
        if not ok:
            cycle_bad.append(m)
    check("EXACT_CYCLE_LAPLACIAN", "structure_dirichlet",
          not cycle_bad, "FINITE_AUDIT", domain=f"1<=M<={bound}",
          failures=cycle_bad)

    audit_bad = {k: [] for k in (
        "rank_nullity_gram", "shift_fixed", "intertwining_iff_divisor",
        "boundary_witness", "invariance_classification",
        "invariance_boundary_witness", "isometry_projection_compression")}
    for (m, d), p in pulls.items():
        c = counts(m, d)
        floor_c = [1 + (m - 1 - r) // d for r in range(d)]
        ceil_c = [-((r-m) // d) for r in range(d)]
        gram = p.H * p
        uniform = gram == sp.Rational(m, d) * sp.eye(d)
        ok = (p.rank() == min(m, d) and d - p.rank() == max(0, d-m)
              and c == floor_c == ceil_c
              and gram == sp.diag(*c) and uniform == (m % d == 0))
        if not ok:
            audit_bad["rank_nullity_gram"].append([m, d])
        # Shift-by-d permutation; its kernel is computed independently.
        s = sp.Matrix(m, m, lambda i, j: int(j == (i+d) % m))
        wdim = m - (s-sp.eye(m)).rank()
        w_in_v = all(in_image(v, m, d) for v in (s-sp.eye(m)).nullspace())
        veq = (s-sp.eye(m))*p == sp.zeros(m, d)
        predicted_equal = (m % d == 0) if d <= m else (d % m == 0)
        if not (wdim == math.gcd(m, d) and w_in_v
                and veq == predicted_equal):
            audit_bad["shift_fixed"].append([m, d])
        residual = laps[m]*p - p*laps[d]
        if (residual == sp.zeros(m, d)) != (m % d == 0):
            audit_bad["intertwining_iff_divisor"].append([m, d])
        if m % d:
            if d <= m:
                target = sp.zeros(1, d)
                target[0, m % d - 1] += 1
                target[0, d - 1] -= 1
                ok = residual[0, :] == target and residual[0, d-1] == -1
            else:
                u = sp.eye(d)[:, m]
                value = (p*laps[d]*u)[m-1]
                ok = p*u == sp.zeros(m, 1) and value == (2 if (m,d)==(1,2) else 1)
            if not ok:
                audit_bad["boundary_witness"].append([m, d])
        invariant = in_image(laps[m]*p, m, d)
        if invariant != (d > m or m % d == 0 or (m,d)==(3,2)):
            audit_bad["invariance_classification"].append([m, d])
        if d <= m and m % d and (m,d)!=(3,2):
            u = sp.eye(d)[:, d-1 if m >= d+2 else 1]
            f = laps[m]*p*u
            if f[0] == f[d]:
                audit_bad["invariance_boundary_witness"].append([m, d])
        if m % d == 0:
            q = m//d
            qq = q_expected[m,d]
            e = qq*qq.H
            avg = sp.Matrix(m, m, lambda i,j: sp.Rational(int(i%d==j%d), q))
            ok = (sp.simplify(qq.H*qq) == sp.eye(d)
                  and sp.simplify(qq.H*laps[m]*qq) == laps[d]
                  and p.H*laps[m]*p == q*laps[d]
                  and e == avg and e == e.H and e*e == e and e*p == p)
            if not ok:
                audit_bad["isometry_projection_compression"].append([m, d])
    groups = {
        "rank_nullity_gram": "EXACT_PULLBACK_STRUCTURE",
        "shift_fixed": "EXACT_PULLBACK_STRUCTURE",
        "intertwining_iff_divisor": "EXACT_INTERTWINING",
        "boundary_witness": "EXACT_INTERTWINING",
        "invariance_classification": "EXACT_INVARIANCE",
        "invariance_boundary_witness": "EXACT_INVARIANCE",
        "isometry_projection_compression": "EXACT_ISOMETRY_COMPRESSION"}
    for name, bad in audit_bad.items():
        check(groups[name], name, not bad, "FINITE_AUDIT",
              domain=f"1<=M,d<={bound}, appropriate branch hypotheses",
              pairs_considered=len(pulls), failures=bad)
    p32 = pulls[3, 2]
    induced = sp.Matrix([[-1, 1], [2, -2]])
    check("EXACT_INVARIANCE", "exception_3_2_induced_operator",
          laps[3]*p32 == p32*induced and induced != laps[2],
          induced=matrix_json(induced), base=matrix_json(laps[2]))
    p53 = pulls[5, 3]
    u53 = sp.Matrix([0, 0, 1])
    check("FALSIFIERS", "5_3_image_not_shift_fixed_and_not_invariant",
          p53*u53 == sp.Matrix([0,0,1,0,0])
          and not in_image(laps[5]*p53*u53,5,3)
          and counts(5,3)==[2,2,1],
          lap_image=matrix_json(laps[5]*p53*u53))
    check("FALSIFIERS", "2_4_whole_image_but_no_intertwining",
          pulls[2,4] == sp.eye(4)[:2,:]
          and laps[2]*pulls[2,4] != pulls[2,4]*laps[4])
    simple2 = sp.Matrix([[-1,1],[1,-1]])
    check("FALSIFIERS", "simple_edge_changes_6_2_intertwining",
          laps[2] == 2*simple2
          and laps[6]*pulls[6,2] != pulls[6,2]*simple2)
    check("FALSIFIERS", "nonuniform_global_normalization_fails",
          sp.Rational(3,5)*(p53.H*p53) != sp.eye(3)
          and pulls[2,4].rank() < 4)
    check("EXACT_ISOMETRY_COMPRESSION", "12_3_consistency",
          pulls[12,3].H*laps[12]*pulls[12,3] == 4*laps[3]
          and q_expected[12,3] == pulls[12,3]/2)

    # Polynomial arithmetic in Q[z]/(z^M-1); no floating trig tolerance.
    z = sp.Symbol("z")
    bad_fourier = []
    for m, a in laps.items():
        vec = sp.Matrix([z**n for n in range(m)])
        lam = z + z**(m-1) - 2
        residual = a*vec - lam*vec
        if any(sp.rem(v, z**m-1, z) != 0 for v in residual):
            bad_fourier.append(m)
    check("FOURIER", "root_of_unity_eigenvectors",
          not bad_fourier, "FINITE_AUDIT",
          domain=f"M=1..{bound}; formal z^M=1", failures=bad_fourier)
    bad_map = []
    for (m,d), qq in q_expected.items():
        p = pulls[m,d]
        base = sp.Matrix([z**r for r in range(d)])
        lifted = sp.Matrix([z**n for n in range(m)])
        if any(sp.rem(v,z**d-1,z) != 0 for v in p*base-lifted):
            bad_map.append([m,d])
    check("FOURIER", "divisor_mode_pullback",
          not bad_map, "FINITE_AUDIT",
          domain=f"d|M, 1<=M,d<={bound}; formal z^d=1",
          failures=bad_map)
    check("FOURIER", "degenerate_base_modes",
          laps[1]*sp.ones(1,1)==sp.zeros(1,1)
          and laps[2]*sp.Matrix([1,-1])==-4*sp.Matrix([1,-1])
          and pulls[6,2]*sp.Matrix([1,-1])==sp.Matrix([1,-1,1,-1,1,-1]))

    # All independent mathematical expectations and audits now exist.
    pre_import_count = len(rows)
    source_before = sha(source)
    spec = importlib.util.spec_from_file_location("_supplement_a_covering", source)
    implementation = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(implementation)
    api_bad = []
    for m, expected in laps.items():
        if implementation.cycle_laplacian(m) != expected:
            api_bad.append(["cycle", m])
    for (m,d), expected in pulls.items():
        if implementation.pullback_matrix(m,d) != expected:
            api_bad.append(["pullback",m,d])
        if m % d == 0:
            if implementation.isometric_pullback(m,d) != q_expected[m,d]:
                api_bad.append(["isometry",m,d])
        elif not throws_value_error(lambda: implementation.isometric_pullback(m,d)):
            api_bad.append(["divisor_gate",m,d])
    check("API_PARITY", "independent_exact_expectations", not api_bad,
          "FINITE_AUDIT", bound=bound, failures=api_bad,
          expectation_construction="completed before source import",
          pre_import_check_records=pre_import_count)
    invalid = [0, -1, 1.5, 1.0, True, False, "3", None]
    validation_bad = []
    for v in invalid:
        funcs = [lambda v=v: implementation.cycle_laplacian(v)]
        for fn in (implementation.pullback_matrix, implementation.isometric_pullback):
            funcs.extend([lambda fn=fn,v=v: fn(v,1), lambda fn=fn,v=v: fn(4,v)])
        if not all(throws_value_error(fn) for fn in funcs):
            validation_bad.append(repr(v))
    class Indexed:
        def __index__(self):
            return 2
    check("API_PARITY", "integer_protocol_and_builtin_bool_handling",
          not validation_bad and implementation.cycle_laplacian(Indexed())==laps[2]
          and implementation.pullback_matrix(sp.Integer(2),sp.Integer(4))==pulls[2,4],
          invalid_rejections=validation_bad,
          semantics="operator.index; explicitly rejects isinstance(value,bool)")
    calls = [lambda: implementation.cycle_laplacian(2),
             lambda: implementation.pullback_matrix(5,3),
             lambda: implementation.isometric_pullback(6,2)]
    objects = []
    for fn in calls:
        a, b = fn(), fn()
        copied = sp.Matrix(a)
        old = a[0,0]
        copied[0,0] += 99
        try:
            a[0,0] = 99
            immutable = False
        except TypeError:
            immutable = True
        objects.append(dict(type=type(a).__name__, shape=list(a.shape),
                            fresh_object=a is not b, immutable=immutable,
                            no_numpy_dtype=not hasattr(a,"dtype"),
                            no_float=not bool(a.atoms(sp.Float)),
                            mutable_copy_isolated=a[0,0]==old))
    check("API_PARITY", "exact_immutable_fresh_matrices",
          all(all(v for k,v in o.items() if k not in ("type","shape"))
              for o in objects), observations=objects)
    check("API_PARITY", "source_content_unchanged_during_import",
          sha(source)==source_before, sha256=source_before)
    head = subprocess.check_output(
        ["git","--no-optional-locks","-C",str(repo),"rev-parse","HEAD"],
        text=True).strip()
    check("INTEGRITY", "expected_head", head==EXPECTED_HEAD,
          "READ_ONLY_RECEIPT", expected=EXPECTED_HEAD, actual=head)
    check("INTEGRITY", "external_paths_and_no_bytecode",
          sys.dont_write_bytecode and not output.is_relative_to(repo)
          and not run_dir.is_relative_to(repo), "READ_ONLY_RECEIPT",
          scratch=str(run_dir), output=str(output))
    if generate_integrity:
        # Full regular-file path/content fingerprints are made AFTER the
        # independent and API checks. Only .git internals are excluded.
        baseline = json.loads(args.fingerprint_before.read_text(encoding="utf-8"))
        external_before = json.loads(args.external_before.read_text(encoding="utf-8"))
        git_before = json.loads(args.git_before.read_text(encoding="utf-8"))
        after, tree_summary, git_after = {}, {}, {}
        aggregate = lambda files: hashlib.sha256(json.dumps(
            files,sort_keys=True,separators=(",",":")).encode()).hexdigest()
        for label, record in baseline.items():
            root = Path(record["root"])
            started = datetime.now(timezone.utc).isoformat()
            files = {}
            for path in sorted(root.rglob("*")):
                rel = path.relative_to(root)
                if path.is_file() and ".git" not in rel.parts:
                    h = hashlib.sha256()
                    with path.open("rb") as handle:
                        for chunk in iter(lambda: handle.read(1048576), b""):
                            h.update(chunk)
                    files[rel.as_posix()] = h.hexdigest()
            after[label] = dict(root=str(root),start_utc=started,
                end_utc=datetime.now(timezone.utc).isoformat(),
                count=len(files),tree_sha256=aggregate(files),files=files)
            before_files = record["files"]
            tree_summary[label] = dict(
                root=str(root),before_count=len(before_files),after_count=len(files),
                before_sha256=aggregate(before_files),after_sha256=aggregate(files),
                unchanged=before_files==files,
                added=sorted(set(files)-set(before_files)),
                removed=sorted(set(before_files)-set(files)),
                modified=[p for p in before_files.keys() & files.keys()
                          if before_files[p]!=files[p]])
            if label in git_before:
                def git(*a):
                    return subprocess.check_output(
                        ["git","--no-optional-locks","-C",str(root),*a],text=True).strip()
                git_after[label] = dict(head=git("rev-parse","HEAD"),
                    tracked_status=git("status","--porcelain","--untracked-files=no"))
            print(f"fingerprint after: {label} {len(files)} {aggregate(files)}",flush=True)
        external_after = {group:{p:sha(p) for p in paths}
                          for group,paths in external_before.items()}
        snapshot_path = args.integrity_receipt.resolve().with_suffix(".after.json")
        with snapshot_path.open("x",encoding="utf-8") as handle:
            json.dump(after,handle,indent=2)
        external_summary = {group:dict(count=len(paths),unchanged=paths==external_after[group],
                                      before_sha256=aggregate(paths),
                                      after_sha256=aggregate(external_after[group]))
                            for group,paths in external_before.items()}
        receipt = dict(
            passed=all(v["unchanged"] for v in tree_summary.values())
                   and external_before==external_after and git_before==git_after,
            method="All regular file relative paths and SHA256 contents; .git components excluded; Git HEAD/tracked status separately",
            tree_summary=tree_summary,external_summary=external_summary,
            git_before=git_before,git_after=git_after,
            before_manifest=dict(path=str(args.fingerprint_before.resolve()),sha256=sha(args.fingerprint_before)),
            after_manifest=dict(path=str(snapshot_path),sha256=sha(snapshot_path)),
            external_before_manifest=dict(path=str(args.external_before.resolve()),sha256=sha(args.external_before)),
            external_after=external_after,
            commits_by_this_task=0,pushes_by_this_task=0,publication=False)
        with args.integrity_receipt.open("x",encoding="utf-8") as handle:
            json.dump(receipt,handle,indent=2)
    receipts = {}
    for label, path in (("integrity",args.integrity_receipt),
                        ("test",args.test_receipt),
                        ("packaging",args.packaging_receipt)):
        if path:
            path = path.resolve()
            value = json.loads(path.read_text(encoding="utf-8"))
            receipts[label] = dict(path=str(path), sha256=sha(path), data=value)
            check("INTEGRITY", label+"_receipt", value.get("passed") is True,
                  "READ_ONLY_RECEIPT", path=str(path))

    witnesses = {}
    for m,d in [(12,3),(6,2),(5,3),(3,2),(2,4),(1,2),(4,1)]:
        p = pulls[m,d]
        a = laps[m]*p
        witnesses[f"{m},{d}"] = dict(
            M=m,d=d,Delta_M=matrix_json(laps[m]),Delta_d=matrix_json(laps[d]),
            P=matrix_json(p),gram=matrix_json(p.H*p),counts=counts(m,d),
            Delta_M_P=matrix_json(a),P_Delta_d=matrix_json(p*laps[d]),
            intertwining_residual=matrix_json(a-p*laps[d]),
            rank=p.rank(),nullity=d-p.rank(),invariant=in_image(a,m,d),
            intertwines=a==p*laps[d],
            Q=matrix_json(q_expected[m,d]) if m%d==0 else None,
            compression=matrix_json(q_expected[m,d].H*laps[m]*q_expected[m,d])
            if m%d==0 else None)
    source_hashes = {str(repo/p):sha(repo/p) for p in SOURCE_RELS}
    source_hashes.update({str(REPORTS/p):sha(REPORTS/p) for p in PRIOR_REVIEW
                          if (REPORTS/p).is_file()})
    passed = all(r["passed"] for r in rows)
    complete_receipts = set(receipts)=={"integrity","test","packaging"}
    group_counts = {}
    for r in rows:
        g=group_counts.setdefault(r["group"],dict(total=0,passed=0))
        g["total"]+=1
        g["passed"]+=int(r["passed"])
    payload = dict(
        schema="trioctagon.supplement_a.exact_results.v0.1",
        generated_utc=datetime.now(timezone.utc).isoformat(),
        scope=["A07","A08","A09"], prior_rows_reassessed=False,
        universal_proof_owner="companion source packet sections 1-13",
        finite_audits_are_universal_proofs=False,
        repo=str(repo),head=head,python=sys.version,executable=sys.executable,
        sympy=sp.__version__,checker_path=str(Path(__file__).resolve()),
        checker_sha256=sha(__file__),passed=passed,
        closeout_ready=passed and complete_receipts,
        check_summary=dict(total=len(rows),passed=sum(r["passed"] for r in rows),
                           groups=group_counts),
        owner_status={k:("FULL" if passed and complete_receipts
                          else "HOLD_PENDING_RECEIPTS_OR_FAILURE") for k in ["A07","A08","A09"]},
        checks=rows,cycle_matrices={str(m):matrix_json(laps[m]) for m in range(1,5)},
        witnesses=witnesses,source_sha256=source_hashes,receipts=receipts)
    output.parent.mkdir(parents=True,exist_ok=True)
    with output.open("x",encoding="utf-8",newline="\n") as handle:
        json.dump(payload,handle,indent=2,ensure_ascii=False)
        handle.write("\n")
    print(json.dumps(dict(output=str(output),passed=passed,
                          checks=len(rows),closeout_ready=payload["closeout_ready"])))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())

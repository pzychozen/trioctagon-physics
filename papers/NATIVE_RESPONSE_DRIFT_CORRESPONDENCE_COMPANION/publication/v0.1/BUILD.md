# Documentary build and verification

The final Windows build used existing Python 3.11.15 in `torment`, Tectonic 0.17.0 and Poppler. No dependencies were installed. From the edition root, using Command Prompt:

```bat
conda activate torment
set PYTHONUTF8=1
set PYTHONDONTWRITEBYTECODE=1
python -B helpers\build.py --build-dir C:\TORMENT\RD_DOCUMENT_REBUILD_01
python -B helpers\verify_document.py --build-dir C:\TORMENT\RD_DOCUMENT_REBUILD_01
```

Choose a fresh build directory outside the edition. `--tectonic` can name an existing compiler; the default records the installed offline compiler used here. Original `--only-cached --untrusted --keep-logs --keep-intermediates` flags are retained. The manuscript/review date and `SOURCE_DATE_EPOCH` are 15 November 2026; actual build timestamps and author activation are separately recorded. A later rebuild must receive its own final-page inspection and file manifest.

Only the seven exact approved status/access replacement groups were applied to the main source. Sections 1-9, all 35 display-math blocks, all three table bodies and the bibliography match the accepted source bytes. The build helper changed one current-status literal. The verification helper changed the current PDF-subject assertion and generated crosswalk-status literal; all substantive checks remain intact.

The final compiler log has no warnings. The newly generated checks cover metadata, text, page numbers, fonts, citations, labels, all relative source targets, source/PDF identities, table hashes and the five-claim crosswalk. Every one of the 11 final pages was rendered and directly inspected. The historical scientific checker, D1 jets, simulations and certificates were not executed; those accepted records remain evidence only.

`records/build/` contains the actual invocation/receipt, stdout, stderr, log and label intermediate needed to audit the final document. `verification/` contains fresh document, render and visual records. No standalone fonts, compiler caches or unrelated operational snapshots are distributed. Historical inherited build/execution records retain their original dates and status.

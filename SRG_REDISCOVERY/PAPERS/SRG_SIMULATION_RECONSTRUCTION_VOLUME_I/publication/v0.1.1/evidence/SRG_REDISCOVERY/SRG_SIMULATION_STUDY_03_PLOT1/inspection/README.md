# Reproduce the inspection, without running a simulation

These scripts read the preserved copies in ../originals. They do not import plot_1.py or 3Dtriangles.py, draw random initial states, call an animation update, or feed a calculated state into another transition.

Use **Command Prompt** and the existing conda environment:

    call C:\Users\Notandi\miniconda3\condabin\conda.bat activate torment
    cd /d C:\TORMENT\TRIOCTAGON_new\trioctagon-physics\SRG_REDISCOVERY\SRG_SIMULATION_STUDY_03_PLOT1
    python -B inspection\analyze_logs.py
    python -B inspection\inspect_movie.py
    python -B inspection\check_visual_correspondence.py
    python -B inspection\inspect_episodes.py
    python -B inspection\independent_checks.py

For independent reproduction, extract a separate copy of the review ZIP and cd to that directory. The five analysis scripts resolve their data paths relative to their own file location. They overwrite only that package's derived analysis, images and library excerpts; original inputs remain read-only. Keep the delivered package intact as the reviewed record.

| Script | Method and outputs |
|---|---|
| analyze_logs.py | Entire physical CSV order; schema/block invariants; all energy/position/GRF identities; deterministic 31-transition velocity-equation sample; event/pair summaries, callback tables, chronology/movement plots |
| inspect_movie.py | Decode all existing MP4 frames, read metadata, save unchanged-resolution RGB stills, captioned sheets and hash ledger |
| check_visual_correspondence.py | Render existing CSV states as fixed tetrahedra; compare original movie0 with all18 existing label-zero states and eight fixed movie frames with B q=f+1; no calculated trajectories |
| inspect_episodes.py | Extract declared short recorded windows; calculate observed mixed-state centroid directions; plot body7's recorded seam window and the historical mixed-axis diagnostic |
| independent_checks.py | Independent stdlib scalar arithmetic for all energy/position/GRF checks and20 original R0 velocity samples; static AST comparison of H/RPCO/GRF; inspect installed Matplotlib callback source |

Software used: Python3.11.15, NumPy2.4.4, Matplotlib3.10.9, OpenCV5.0.0, Pillow and imageio-ffmpeg's bundled FFmpeg7.1. Full version details are recorded in the manifest environment. The movie contact-sheet script uses C:/Windows/Fonts/arial.ttf. Another platform/font/rendering version may change derived-image pixels without changing the original evidence. No dependency installation was performed.

The FFmpeg metadata call is input-only; its “at least one output file” message is expected and is retained in movie_container_metadata.txt. Successful OpenCV decoding of all200 frames is checked separately.

finalize_package.py is a preservation/packaging utility for the authoritative repository, not a dynamics checker. It verifies the119 protected original/prior-package files, Git HEAD/index/status, exact copies, frame hashes and document links; snapshots the ledger; writes the manifest; creates the ZIP and reads every member back. It requires the original workspace and prior preservation snapshot. Do not use it to replace the delivered evidence with a differently located archive.

verify_delivery.py checks the manifest/ZIP hashes and CRCs after packaging and writes no files. It can be used on an intact delivered directory; the archive is not recursively included in itself.

Numerical outputs are full precision. Rounded report values, selected frames and derived charts are navigation aids. The original CSVs remain the primary chronology.

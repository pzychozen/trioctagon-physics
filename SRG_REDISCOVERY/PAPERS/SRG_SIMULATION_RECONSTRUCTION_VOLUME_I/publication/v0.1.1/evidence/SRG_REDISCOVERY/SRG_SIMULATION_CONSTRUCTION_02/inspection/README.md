# Inspection reproducibility

All Python commands in this checkpoint ran through Command Prompt with the torment Conda environment active. No original source was imported or executed, and no animation instance or simulated transition was created.

From Command Prompt:

    call C:\Users\Notandi\miniconda3\condabin\conda.bat activate torment
    cd /d C:\TORMENT\TRIOCTAGON_new\trioctagon-physics
    python -B SRG_REDISCOVERY\SRG_SIMULATION_CONSTRUCTION_02\inspection\inspect_environment.py
    python -B SRG_REDISCOVERY\SRG_SIMULATION_CONSTRUCTION_02\inspection\inspect_video.py
    python -B SRG_REDISCOVERY\SRG_SIMULATION_CONSTRUCTION_02\inspection\inspect_early_movie.py
    python -B SRG_REDISCOVERY\SRG_SIMULATION_CONSTRUCTION_02\inspection\inspect_jump_window.py
    python -B SRG_REDISCOVERY\SRG_SIMULATION_CONSTRUCTION_02\inspection\verify_sources.py

These helpers read the copied movie or historical sources and write only derived inspection files in this package. The three video scripts decode existing media. The environment script reads installed library functions and evaluates H at two scalar arguments; it does not evolve a state. The source checker parses syntax and compares function bodies while ignoring docstrings.

The early same-color-phase inspection followed the full-duration overview. The consecutive 8–16 window followed the observed relocation between same-phase samples 8 and 16. This was inspection of one surviving recording, not a search over seeds, parameters or new trajectories.

environment.json records Python, NumPy, Matplotlib and paths. OpenCV 5.0.0 decoded the movie. A bundled imageio-ffmpeg binary reported its metadata; no software was installed. Full-resolution PNGs are decoded movie frames. The four contact sheets additionally resize them and add frame/time labels using Pillow.

static_source_checks.json certifies both copied programs against their originals and confirms identical H and RPCO syntax apart from docstrings. provenance_excerpts.txt preserves the narrow pre-existing index/report and filename-disambiguation evidence used in this review.

preservation_before.json is the pre-work repository/index/status baseline plus protected-file hashes. preservation_after.json is the final comparison. finalize_package.py checks these records, source/media identity, extraction-ledger hashes and document links, then constructs and reads back the review ZIP. It contains no simulation code. Its preservation check is specific to this workspace baseline and should not be treated as a portable simulation launcher.

MANIFEST.json lists all payload files with hashes except itself and the enclosing ZIP, avoiding recursive self-hashing. The ZIP contains the manifest and every other package file.

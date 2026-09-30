"""Installed launcher; bounded smoke builds the shell without scientific execution."""
import argparse
import json
import os
import sys


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--smoke-test", action="store_true")
    args = parser.parse_args(argv)
    attempts = []
    def audit(event, values):
        if event in ("socket.connect", "socket.getaddrinfo", "urllib.Request"):
            attempts.append(event)
            raise RuntimeError("Normal application runtime is offline")
    sys.addaudithook(audit)
    os.environ.setdefault("QT_OPENGL", "software")
    if args.smoke_test:
        os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
    from trioctagon_ui.qt_runtime import prepare_qt
    prepare_qt()
    from PySide6.QtCore import QTimer
    from PySide6.QtWidgets import QApplication
    from trioctagon_ui.app import MainWindow
    app = QApplication.instance() or QApplication(["trioctagon-scientific-ui"])
    window = MainWindow()
    if args.smoke_test:
        assert window.tabs.count() == 4 and window.help["items"]
        assert not window.run_button.isEnabled() and not window.jobs.busy
        assert not any(n.startswith(("torch", "tensorflow", "transformers")) for n in sys.modules)
        QTimer.singleShot(50, app.quit)
    else:
        window.show()
    code = app.exec()
    if args.smoke_test:
        print(json.dumps({"status": "PASS", "workspaces": window.tabs.count(), "help_loaded": True,
                          "scientific_jobs_submitted": 0, "runtime_network_attempts": attempts,
                          "isolated": bool(sys.flags.isolated), "model_required": False, "gpu_required": False}))
    return code


if __name__ == "__main__":
    raise SystemExit(main())

"""One installed scientific subprocess; atomic completion and bounded cancellation."""
import json
from pathlib import Path
import sys
import tempfile
import time

from PySide6.QtCore import QObject, QProcess, QProcessEnvironment, QTimer, Signal
from trioctagon_ui.record_views import atomic_text
from trioctagon_ui.requests import validate_envelope


def validate_response(response, request):
    if not isinstance(response, dict) or type(response.get("ui_response_version")) is not int or response["ui_response_version"] != 1:
        raise ValueError("Incomplete worker response envelope")
    if response.get("isolated") is not True or response.get("imports") != {"gui": [], "models": []} or response.get("runtime_network_attempts") != []:
        raise ValueError("Missing or failed worker isolation/GUI/model/network audit")
    if any(response.get(key) != request[key] for key in ("request_id", "operation")):
        raise ValueError("Worker response belongs to a different request")
    if response.get("status") == "completed":
        result = response.get("result", {})
        required = {"canonical_json", "record_type", "deterministic_sha256", "source_commit", "produced_current"}
        if set(result) != required or not isinstance(result["canonical_json"], str) or type(result["produced_current"]) is not bool:
            raise ValueError("Incomplete completed-record response")
        data = json.loads(result["canonical_json"])
        if data.get("record_type") != result["record_type"] or data.get("deterministic_sha256") != result["deterministic_sha256"] or data.get("implementation", {}).get("commit") != result["source_commit"]:
            raise ValueError("Worker envelope and canonical record disagree")
    elif response.get("status") == "failed":
        if not all(isinstance(response.get("error", {}).get(k), str) for k in ("exception_class", "message")):
            raise ValueError("Incomplete worker failure details")
    else:
        raise ValueError("Unknown or partial worker status")
    if response.get("imports", {}).get("gui") or response.get("imports", {}).get("models") or response.get("runtime_network_attempts"):
        raise ValueError("Worker violated the GUI/model/network boundary")
    return response


class JobManager(QObject):
    state_changed = Signal(str)
    elapsed_changed = Signal(float)
    completed = Signal(dict)
    failed = Signal(dict)
    cancelled = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.process = None
        self.state = "idle"
        self.request = None
        self.stderr = ""
        self.stdout = ""
        self._cancel = False
        self._terminal = False
        self._files = None
        self.timer = QTimer(self)
        self.timer.setInterval(200)
        self.timer.timeout.connect(lambda: self.elapsed_changed.emit(time.monotonic() - self.started_at))

    @property
    def busy(self):
        return self.process is not None

    def _state(self, value):
        self.state = value
        self.state_changed.emit(value)

    def start(self, envelope):
        if self.busy:
            raise ValueError("A scientific worker is already active")
        validate_envelope(envelope)
        self._state("validating")
        self.request = json.loads(json.dumps(envelope, allow_nan=False))
        self._files = tempfile.TemporaryDirectory(prefix="trioctagon-ui-job-")
        self.directory = Path(self._files.name)
        self.response_path = self.directory / "response.json"
        atomic_text(self.directory / "request.json", json.dumps(self.request, ensure_ascii=False, allow_nan=False))
        self._cancel = self._terminal = False
        self.stderr = self.stdout = ""
        self.started_at = time.monotonic()
        process = QProcess(self)
        self.process = process
        env = QProcessEnvironment.systemEnvironment()
        env.remove("PYTHONPATH")
        env.insert("PYTHONUTF8", "1")
        process.setProcessEnvironment(env)
        process.setWorkingDirectory(str(self.directory))
        process.setProgram(str(Path(sys.executable).resolve()))
        process.setArguments(["-I", "-B", "-m", "trioctagon_ui.worker", "--request",
                              str(self.directory / "request.json"), "--response", str(self.response_path)])
        process.started.connect(lambda: self._state("running") if not self._cancel else None)
        process.readyReadStandardError.connect(self._drain)
        process.readyReadStandardOutput.connect(self._drain)
        process.finished.connect(self._finish)
        process.errorOccurred.connect(self._process_error)
        self.timer.start()
        process.start()

    def _drain(self):
        if self.process is not None:
            self.stderr += bytes(self.process.readAllStandardError()).decode("utf-8", errors="replace")
            self.stdout += bytes(self.process.readAllStandardOutput()).decode("utf-8", errors="replace")

    def _process_error(self, error):
        if error == QProcess.ProcessError.FailedToStart:
            self.stderr += self.process.errorString()
            self._finish(-1, QProcess.ExitStatus.CrashExit)

    def cancel(self):
        if self.process is None or self._terminal:
            return
        self._cancel = True
        process = self.process
        process.terminate()
        QTimer.singleShot(1000, lambda: process.kill() if self.process is process and process.state() != QProcess.ProcessState.NotRunning else None)

    def _finish(self, code, exit_status):
        if self._terminal:
            return
        self._terminal = True
        self.timer.stop()
        self._drain()
        process = self.process
        self.process = None
        files, self._files = self._files, None
        try:
            if self._cancel:
                self._state("cancelled")
                self.cancelled.emit()
                return
            response = validate_response(json.loads(self.response_path.read_text(encoding="utf-8")), self.request)
            if response["status"] == "completed" and code == 0 and exit_status == QProcess.ExitStatus.NormalExit:
                self._state("completed")
                self.completed.emit(response)
                return
            error = response.get("error", {"exception_class": "ChildProcessError", "message": f"Worker exited with code {code}"})
        except Exception as exc:
            error = {"exception_class": type(exc).__name__, "message": str(exc)}
        finally:
            if process is not None:
                process.deleteLater()
            if files is not None:
                files.cleanup()
        self._state("failed")
        self.failed.emit({**error, "operation": self.request["operation"], "request_id": self.request["request_id"],
                          "stderr": self.stderr, "stdout": self.stdout})

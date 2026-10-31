"""Read-only compatibility check; stay in torment, no installation or output PDF."""
import pathlib,sys
BUNDLE=pathlib.Path(r'C:\Users\Notandi\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\site-packages')
sys.path.append(str(BUNDLE))
import reportlab
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph,SimpleDocTemplate
from reportlab.lib import rl_accel
print('interpreter',sys.executable)
print('reportlab',reportlab.Version,reportlab.__file__)
print('pdf_pure_python_available',bool(canvas.Canvas and Paragraph and SimpleDocTemplate))
print('acceleration_module',rl_accel.__file__)

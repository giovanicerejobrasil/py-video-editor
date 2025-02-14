from PySide6.QtWidgets import QApplication
from editor.window import MainWindow
import sys

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())

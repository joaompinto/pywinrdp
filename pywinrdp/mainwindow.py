import sys

from PyQt5.QtWidgets import QMainWindow
from .axwidget import AxWidget


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)
        self.setWindowTitle("Python Remote Desktop")
        self.ax_widget = AxWidget()
        # Set the central widget of the Window.
        self.setCentralWidget(self.ax_widget)

    def closeEvent(self, event):
        self.ax_widget.closeEvent(event)

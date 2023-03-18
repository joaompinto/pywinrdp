import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtAxContainer import QAxWidget


def window():
    app = QApplication(sys.argv)
    RDP_Widget = QAxWidget("MsTscAx.MsTscAx")
    RDP_Widget.setProperty("Server", "192.168.33.10")
    RDP_Widget.setProperty("UserName", "vagrant")
    RDP_Widget.resize(800, 600)
    RDP_Widget.show()
    RDP_Widget.dynamicCall("Connect()")
    sys.exit(app.exec())


if __name__ == "__main__":
    window()

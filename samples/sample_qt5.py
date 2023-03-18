import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QAxContainer import QAxWidget


def window():
    app = QApplication(sys.argv)
    RDP_Widget = QAxWidget("MsTscAx.MsTscAx")
    RDP_Widget.setProperty("Server", "192.168.33.10")
    RDP_Widget.setProperty("UserName", "vagrant")
    RDP_Widget.resize(800, 600)
    RDP_Widget.show()
    RDP_Widget.Connect()
    sys.exit(app.exec_())


if __name__ == "__main__":
    window()

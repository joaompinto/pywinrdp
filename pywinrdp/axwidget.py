from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton
from .rdpwidget import RemoteDesktopWidget


class AxWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super(AxWidget, self).__init__(*args, **kwargs)
        layout = QVBoxLayout(self)
        self.rdp_widget = RemoteDesktopWidget(self)
        self.bottom_button = QPushButton("Connect", self, clicked=self.onConnectClicked)
        layout.addWidget(self.rdp_widget)
        layout.addWidget(self.bottom_button)
        # https://learn.microsoft.com/en-us/windows/win32/termserv/imstscaxevents-methods
        self.rdp_widget.OnConnecting.connect(self.OnConnecting)
        self.rdp_widget.OnConnected.connect(self.OnConnected)
        self.rdp_widget.OnDisconnected.connect(self.OnDisconnected)
        self.rdp_widget.OnFatalError.connect(self.OnFatalError)
        self.rdp_widget.OnAutoReconnecting.connect(self.OnAutoReconnecting)
        self.is_connected = False

    def onConnectClicked(self):
        self.bottom_button.setText("Disconnect")
        if not self.is_connected:
            self.rdp_widget.SetLogin("192.168.33.10", "vagrant")
            self.rdp_widget.Connect()
        else:
            self.rdp_widget.Disconnect()

    def OnFatalError(self, reason):
        print(f"Fatal Error: {reason}")

    def OnAutoReconnecting(self, reason):
        print(f"OnAutoReconnecting")

    def OnConnected(self):
        self.is_connected = True

    def OnConnecting(self):
        print("Connecting")

    def OnDisconnected(self, reason):
        self.is_connected = False
        print(f"Disconnected for {reason}")

    def OnLogonError(self):
        print("Logon Error")

    def closeEvent(self, event):
        self.rdp_widget.clear()

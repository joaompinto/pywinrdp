"""
This module implements an Remote Desktop Widget using the ActiveX controller:
    https://learn.microsoft.com/en-us/windows/win32/termserv/mstscax
"""
from PyQt5.QAxContainer import QAxWidget


class RemoteDesktopWidget(QAxWidget):
    def __init__(self, parent, SmartSizing=True):
        super(RemoteDesktopWidget, self).__init__(parent)
        self.setControl("MsTscAx.MsTscAx")
        RDP_Advanced_Settings = self.querySubObject("AdvancedSettings")
        RDP_Advanced_Settings.setProperty("SmartSizing", SmartSizing)
        RDP_Advanced_Settings.setProperty("GrabFocusOnConnect", True)

    def SetLogin(self, server, username):
        self.setProperty("Server", server)
        self.setProperty("UserName", username)

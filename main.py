
import sys,random,os,math
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore

from PyQt5 import QtWebEngineWidgets
from PyQt5.QtCore import QTime, QTimer, Qt, pyqtSignal

import sprite
import character

class DesktopPet(QtWidgets.QWidget):
    def __init__(self, parent=None, **kwargs):
        super(QtWidgets.QWidget, self).__init__(parent)

        self.sprite_dict = {}

        # 设置透明窗口
        # self.setWindowFlags(Qt.FramelessWindowHint|Qt.WindowStaysOnTopHint|Qt.SubWindow)
        # self.setAutoFillBackground(False)
        # self.setAttribute(Qt.WA_TranslucentBackground, True)
        # self.repaint()
        # 设置小菜单
        self.tray_icon_menu = QtWidgets.QMenu(self)
        self.tray_icon = QtWidgets.QSystemTrayIcon(self)
        self.tray_icon.setIcon(QtGui.QIcon("./asset/gui/index.png"))
        self.tray_icon.setContextMenu(self.tray_icon_menu)
        self.tray_icon.show()
        # 退出按钮
        quite_act = QtWidgets.QAction('Exit',self,triggered=self.quit)
        quite_act.setIcon(QtGui.QIcon("./asset/gui/close.png"))
        self.tray_icon_menu.addAction(quite_act)

        self.setSprites()

    def setSprites(self):
        sikadi_blue = character.Character(self.tray_icon_menu,"sikadi_blue")
        sikadi_blue.setSprite()
        sikadi_blue.run()
        self.sprite_dict["sikadi_blue"] = sikadi_blue

        # sikadi_blue = character.Character(self.tray_icon_menu,"sikadi_blue")
        # sikadi_blue.setSprite()
        # sikadi_blue.setMenu()
        # sikadi_blue.run()
        # self.sprite_dict["sikadi_blue2"] = sikadi_blue

    def quit(self):
        self.close()
        sys.exit()

if __name__ =="__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = DesktopPet()
    sys.exit(app.exec())
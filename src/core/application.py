
import sys
import random
import os
import math
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore

from PyQt5 import QtWebEngineWidgets
from PyQt5.QtCore import QTime, QTimer, Qt, pyqtSignal

from src.character import sprite
from src.character import character
from src.utils.constants import UI_ICONS_DIR

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
        self.tray_icon.setIcon(QtGui.QIcon(os.path.join(UI_ICONS_DIR, "index.png")))
        self.tray_icon.setContextMenu(self.tray_icon_menu)
        self.tray_icon.show()
        # 退出按钮
        quite_act = QtWidgets.QAction('Exit',self,triggered=self.quit)
        quite_act.setIcon(QtGui.QIcon(os.path.join(UI_ICONS_DIR, "close.png")))
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
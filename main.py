"""
桌宠应用程序主入口
"""
import sys
import os
from PyQt5 import QtWidgets

# 添加src目录到Python路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.core.application import DesktopPet

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = DesktopPet()
    sys.exit(app.exec())

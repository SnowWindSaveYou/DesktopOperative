
import sys,random,os,math
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore

from PyQt5 import QtWebEngineWidgets
from PyQt5.QtCore import QTime, QTimer, Qt, pyqtSignal



import animation
import dialog

SOUND_FILE = "Sound"
IDLE_STATE = "Idle"
START_STATE = "Start"
MOVE_STATE = "Move"
INTERACT_STATE = "Interact"
SPERITE_DIR = "./asset/sprite/sikadi_blue"

class Sperite(QtWidgets.QWidget):
    long_pressed = pyqtSignal()
    def __init__(self,  menu=None, name=None,
                        w=300,h=300, 
                        parent=None,**kwargs):
        super(QtWidgets.QWidget, self).__init__(parent)
        # 初始化
        self.menu = menu
        self.name = name
        self.w = w
        self.h = h
        self.state = START_STATE
        self.isHold = False
        self.mouse_pos = None
        self.sprite_dir = os.path.join("./asset/sprite",name)

        self.interval = 125

        # 设置透明窗口
        self.setWindowFlags(Qt.FramelessWindowHint|Qt.WindowStaysOnTopHint|Qt.SubWindow)
        self.setAutoFillBackground(False)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.repaint()

        # self.setMenu()
        # self.setSprite()
        # self.run()

    def runTime(self):
        # 运行过程
        frame_state = self.anim.update(self.state)
        if self.isHold:
            self.state = MOVE_STATE
        elif frame_state["isEnd"]:
            self.state = IDLE_STATE
        pass
    

    def setSprite(self,sprite_dir=None):
        # 设置sprite角色
        if sprite_dir is not None:
            self.sprite_dir = sprite_dir
        self.image_lab = QtWidgets.QLabel(self)
        self.anim = animation.Animation(
            self.image_lab,
            self.sprite_dir,
            self.state,
            self.w,self.h)
        pass

    def run(self):
        # 显示
        self.display()
        # 运行程序
        self.runTimer = QTimer()
        self.runTimer.timeout.connect(self.runTime)
        self.runTimer.start(self.interval)
        # 长按监听
        self.long_press_timer = QTimer()
        self.long_press_timer.timeout.connect(self._long_pressed)

    def setMenu(self):
        # 退出按钮
        quite_act = QtWidgets.QAction('%s Exit'%(self.name),self,triggered=self.quit)
        quite_act.setIcon(QtGui.QIcon("./asset/gui/close.png"))
        self.menu.addAction(quite_act)

    def mousePressEvent(self, e):
        # 设置长按监听
        super().mousePressEvent(e)
        self.mouse_pos = e.globalPos()- self.pos()
        e.accept()
        self.long_press_timer.start(300)


    def mouseReleaseEvent(self, e):
        # 判断长按
        if self.long_press_timer.remainingTime()<=0:
            self.long_press_timer.blockSignals(True)
        self.long_press_timer.stop()
        super().mouseReleaseEvent(e)
        self.long_press_timer.blockSignals(False)
        if (self.isHold):
            self.isHold = False
        else:
            print("clicked")
            self.state = INTERACT_STATE
        self.setCursor(QtGui.QCursor(Qt.ArrowCursor))

    def mouseMoveEvent(self, e):
        if Qt.LeftButton and self.isHold:
            aim_pos = e.globalPos()- self.mouse_pos
            # aim_dir = (aim_pos-self.pos())
            # aim_dir = aim_dir/aim_dir.manhattanLength()
            # # print(aim_dir)
            # self.move(self.pos()+3*aim_dir)
            self.move(aim_pos)
            e.accept()

    def _long_pressed(self):
        self.long_press_timer.stop()
        self.long_pressed.emit()
        print("long pressed")
        self.isHold = True
        self.setCursor(QtGui.QCursor(Qt.OpenHandCursor))

    def display(self):
        self.resize(self.w,self.h)
        screen_geo = QtWidgets.QDesktopWidget().screenGeometry()
        pet_geo = self.geometry()
        width = int((screen_geo.width()-pet_geo.width())*random.random())
        height = int((screen_geo.height()- pet_geo.height())*random.random())
        self.move(width,height)
        self.show()
    def quit(self):
        self.close()
        sys.exit()

# if __name__ =="__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     widget = Sperite("./asset/sprite/sikadi_blue")
#     sys.exit(app.exec())
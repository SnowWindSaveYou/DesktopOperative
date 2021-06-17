from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore

from PyQt5 import QtWebEngineWidgets
from PyQt5.QtCore import QPoint, QThread, QTime, QTimer, Qt, pyqtSignal
from functools import partial  


class Dialog(QtWidgets.QDialog):
    def __init__(self,content,options,pos,signal,duration=500,w=200,h=80,**kwargs):
        super(Dialog, self).__init__()
        self.signal = signal
        self.duration= duration
        self.btn_list = []
        # 设置样式
        self.resize(w,h)
        self.setWindowFlags(Qt.FramelessWindowHint|Qt.WindowStaysOnTopHint|Qt.SubWindow)
        self.setWindowOpacity(0.85)
        self.setContentsMargins(0, 0, 0, 0)
        self.setObjectName("EventDialog")
        # self.setStyleSheet("background-color:black; color:white;margin:0;font-size:11px;")
        self.layer = QtWidgets.QVBoxLayout(self)
        self.layer.setContentsMargins(0, 0, 0, 0)
        # self.layer.setAlignment(Qt.AlignCenter)
        # self.layer.setObjectName("MainLayer")
        self.styleSheet_ = """
            #EventDialog {
                background-color:black; 
                color:white;
                margin:0px;
                padding:0px;
                font-size:11px;
            }
            #progress {
                margin:0px;
                padding:0px;
                top:0px;
                left:0px;
                max-height: 3px;
            }
            #progress::chunk {
                background-color: #2196f3;
            }
            #content{
                background-color:black; 
                padding:5px;
                color:white;
                font-size:11px;
            }
            #option{
                background-color:black; 
                color:white;
                font-size:11px;
            }
            #option::hover{
                border-style:solid;
                border-width:1px;
                border-color: white;
            }
        """

        # 进度条
        self.progress = QtWidgets.QProgressBar(self,minimum=0,maximum=self.duration,objectName="progress")
        self.progress.setTextVisible(False)
        self.progress.setContentsMargins(0, 0, 0, 0)
        self.layer.addWidget(self.progress)
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateProgress)
        self.timer.start(10)

        # 内容和选项
        content = QtWidgets.QLabel(content,objectName="content")
        content.setWordWrap(True)
        self.layer.addWidget(content)
        for i in range(len(options)):
            btn = QtWidgets.QPushButton(self,objectName="option")
            btn.setText(""+str(options[i]))
            btn.clicked.connect(partial( self.emit,i))
            self.layer.addWidget(btn)
        
        self.setStyleSheet(self.styleSheet_)
        self.show()
        self.move(pos)

    def updateProgress(self):
        # 刷新进度条
        val = self.progress.value()
        if val <self.duration:
            self.progress.setValue(val+1)
        else:
            self.timer.stop()
            self.signal.emit(-1)
    def emit(self,i):
        self.signal.emit(i)
        return i
    def move(self,a0:QPoint):
        # 加上窗口高度防覆盖
        a0+=QPoint(0,-self.geometry().height())
        super().move(a0)
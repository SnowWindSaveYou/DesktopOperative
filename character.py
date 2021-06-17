import os
import random
from typing_extensions import runtime
from PyQt5.QtCore import QPoint, pyqtSignal
import sprite
import dialog
import event_manager
SOUND_FILE = "Sound"
IDLE_STATE = "Idle"
START_STATE = "Start"
MOVE_STATE = "Move"
INTERACT_STATE = "Interact"
SPERITE_DIR = "./asset/sprite/sikadi_blue"

NORMAL_EMOTION = "Normal"
Angry_EMOTION = "Angry"

class Character(sprite.Sperite):
    on_event_complete= pyqtSignal(int)
    def __init__(self, menu, name, w=300, h=300, parent=None, **kwargs):
        super().__init__(menu=menu, name=name, w=w, h=h, parent=parent, **kwargs)
        self.state = START_STATE
        self.dia = None
        self.event = -1
        self.emotion= NORMAL_EMOTION
        self.event_manager = event_manager.EventManager(os.path.join("./achieves","%s.json"%str(name)),self.sprite_dir)
        self.on_event_complete.connect(self.onEventCompelete)
    def runTime(self):
        # 运行过程
        frame_state = self.anim.update(self.state)
        if self.isHold:
            self.state = MOVE_STATE
        elif frame_state["isEnd"]:
            if( (self.state not in [MOVE_STATE,START_STATE])
                and (self.event ==-1) 
                and (random.random()>0.5)):
                self.randomEvent()
            else:
                self.state = IDLE_STATE
        pass

    def mouseMoveEvent(self, e):
        """
        让对话框一起移动
        """
        super().mouseMoveEvent(e)
        if self.dia is not None:
            self.dia.move(self.pos()+QPoint(50,100))

    def randomEvent(self):
        event = self.event_manager.getRandomEvent()
        self.executeEvent(event)
        
    def executeEvent(self,event):
        """
        处理事件
        """
        self.event = event
        if "state" in event:
            self.state =event["state"]
        self.dia = dialog.Dialog(  event["content"],[i["option"] for i in event["options"]],
                                self.pos()+QPoint(50,75),
                                self.on_event_complete,
                                event["duration"] if "duration" in event else 500
                                )
    def onEventCompelete(self,idx):
        """
        事件解决后销毁对话框，并执行下一个事件
        """
        event = self.event_manager.eventNext(self.event,idx)
        self.dia.close()
        self.event = event
        if event==-1:
            return
        else:
            self.executeEvent(event)
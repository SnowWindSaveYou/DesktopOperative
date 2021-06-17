import os,json,random

from PyQt5.QtCore import pyqtSignal
import dialog
"""
通过当前角色的flag过滤可执行的事件
on:[条件] 
No=禁止随机触发
"""



class EventManager():
    
    def __init__(self,achieve_dir,sprite_dir) -> None:
        self.achieve_dir = achieve_dir
        self.event_dir = os.path.join(sprite_dir,"Events")

        self.events = dict()
        self.loadAchieve()
        self.loadEvents()
        pass
    def loadAchieve(self):
        with open(self.achieve_dir) as f:
            self.achieve = json.load(f)

    def loadEvents(self):
        listdir = os.listdir(self.event_dir)
        for d in listdir:
            file_path = os.path.join(self.event_dir,d)
            print(file_path)
            with open(file_path, encoding='UTF-8') as f:
                json_dict = dict(json.load(f))
                print(json_dict)
                self.events.update(json_dict)

    def isOk(self,event):
        """
        判断事件是否能够执行
        """
        if ("req" not in event) or (len(event["req"])==0):
            return True

        for r in event["req"]:
            if r== "No":
                return False
            if r not in self.achieve.flags:
                return False
        return True

    def getRandomEvent(self):
        OK = False
        while not OK:
            event_key = random.sample(self.events.keys(),1)[0]
            event = self.events[event_key]
            if self.isOk(event):
                if "options" not in event:
                    event["options"] =[]
                return event
    def getEvent(self,event_key):
        if event_key not in self.events:
            return -1
        event = self.events[event_key]
        if "options" not in event:
            event["options"] =[]
        return self.events[event_key]

    def eventNext(self,event,option_idx):
        if(option_idx== -1):
            return -1
        event = event["options"][option_idx]
        if "next" in event:
            return self.getEvent(event["next"])
        return -1
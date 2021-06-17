from genericpath import isfile
from PyQt5 import QtGui
import os,sys

IMAGES_DIR = "Images"


class Animation():
    def __init__(self,canvas,dir,state,w=200,h=200) -> None:
        self.canvas = canvas
        self.dir = os.path.join(dir,IMAGES_DIR)
        self.state = state
        self.w = w
        self.h = h
        self.sp_dict = {}
        self.cur_idx = 0
        self.img_buff = []
        self.readPath()
        self.loadImgBuff()
        self.update(self.state)
        pass
    def readPath(self):
        # 读取图片列表长度
        listdir = os.listdir(self.dir)
        for d in listdir:
            file_path = os.path.join(self.dir,d)
            if not os.path.isfile(file_path):
                self.sp_dict[d] = len(os.listdir(file_path))
        print(self.sp_dict)
        # # 读取音频列表名字
        # self.sp_dict[SOUND_FILE] = os.listdir(os.path.join(self.dir,SOUND_FILE))
        pass

    def changeState(self,state):
        self.state = state
        self.cur_idx = 0
        self.loadImgBuff()
        pass

    def loadImgBuff(self):
        # 状态帧缓存 
        # TODO 多线程加载
        self.img_buff =[]
        for i in range(self.sp_dict[self.state]):
            image = QtGui.QImage()
            image.load(os.path.join(self.dir,self.state, "%04d.png"%(i+1)))
            image = image.scaled(self.w,self.h)
            self.img_buff.append(image)

    def getCurIdx(self):
        idx = self.cur_idx
        self.cur_idx+=1
        if(self.cur_idx>= self.sp_dict[self.state]):
            self.cur_idx= 0
        return idx

    def setFrame(self,frame):
        self.canvas.setPixmap(QtGui.QPixmap.fromImage(frame))

    def update(self,state):
        if state!= self.state:
            self.changeState(state)
        # 更新当前帧
        self.setFrame(self.img_buff[self.cur_idx])
        # 更新索引
        isEnd = False
        self.cur_idx+=1
        if(self.cur_idx>= self.sp_dict[self.state]):
            self.cur_idx= 0
            isEnd = True
        return {
            "state":self.state,
            "idx":self.cur_idx+1,
            "isEnd":isEnd
        }


if __name__ =="__main__":
    sp = Animation("asset\sprite\sikadi_blue")

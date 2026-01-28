"""
常量定义文件
"""
import os

# 路径常量
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
DATA_DIR = os.path.join(BASE_DIR, "data")
CONFIG_DIR = os.path.join(BASE_DIR, "config")

# 资源路径
CHARACTERS_DIR = os.path.join(ASSETS_DIR, "characters")
UI_ICONS_DIR = os.path.join(ASSETS_DIR, "ui", "icons")
CHARACTER_DATA_DIR = os.path.join(DATA_DIR, "characters")

# 状态常量
IDLE_STATE = "Idle"
START_STATE = "Start"
MOVE_STATE = "Move"
INTERACT_STATE = "Interact"
ATTACK_STATE = "Attack"
SIT_STATE = "Sit"
LOSS_STATE = "Loss"

# 情感常量
NORMAL_EMOTION = "Normal"
AMAZING_EMOTION = "Amazing"
ANGRY_EMOTION = "Angry"
LOSS_EMOTION = "Loss"
HAPPY_EMOTION = "Happy"
SHY_EMOTION = "Shy"

# 动画相关
IMAGES_DIR = "Images"
SOUND_FILE = "Sound"
EMOTIONS_DIR = "Emotions"
EVENTS_DIR = "Events"

# UI常量
DEFAULT_PET_WIDTH = 300
DEFAULT_PET_HEIGHT = 300
DEFAULT_DIALOG_WIDTH = 200
DEFAULT_DIALOG_HEIGHT = 80
DEFAULT_ANIMATION_INTERVAL = 125
DEFAULT_DIALOG_DURATION = 500

# 颜色和样式
DIALOG_BACKGROUND_COLOR = "black"
DIALOG_TEXT_COLOR = "white"
DIALOG_BORDER_COLOR = "#2196f3"
DIALOG_OPACITY = 0.85

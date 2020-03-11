from enum import Enum
from libs.emotions import *

class EmotionEnum(Enum):
    ANGRY = Angry()
    EXCITEMENT = Excitement()
    FEAR = Fear()
    HAPPY = Happy()
    PLEASANT = Pleasant()
    SURPRISE = Surprise()
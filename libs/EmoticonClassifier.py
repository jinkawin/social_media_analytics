import numpy as np
import pandas as pd

from django.conf import settings

from .NrcProcess import NrcProcess
from libs.emotions.EmotionEnum import EmotionEnum

class EmoticonClassifier(NrcProcess):
    IS_DEBUG = False

    def __init__(self):
        super().__init__()

    def classify(self, sentence):
        emotions = {}
        for emotion in EmotionEnum:
            emoticons = emotion.value.EMOTICONS
            if any(emoticon in sentence for emoticon in emoticons):
                emotions[emotion.value.NAME] = 1

        if self.IS_DEBUG: print("Emoticons: ")
        if self.IS_DEBUG: self.printDict(emotions)
        return emotions
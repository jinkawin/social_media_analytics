import numpy as np
import pandas as pd

from django.conf import settings

from .NrcProcess import NrcProcess
from libs.emotions.EmotionEnum import EmotionEnum

class EmoticonClassifier(NrcProcess):

    def __init__(self):
        super().__init__()

    def classify(self, sentence):
        emotions = {}
        for emotion in EmotionEnum:
            emoticons = emotion.value.EMOTICONS
            if any(emoticon in sentence for emoticon in emoticons):
                emotions[emotion.value.NAME] = 1

        # print("Emoticons: ")
        # self.printDict(emotions)
        return emotions
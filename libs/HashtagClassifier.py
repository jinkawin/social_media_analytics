import numpy as np
import pandas as pd

from django.conf import settings

from .NrcProcess import NrcProcess

class HashtagClassifier(NrcProcess):
    IS_DEBUG = False

    def __init__(self):
        super().__init__()

    def classify(self, hashtags):
        score = {}
        for hashtag in hashtags:
            if self.IS_DEBUG: print("hashtag: ", hashtag)

            _score = self.getHashtagScore(hashtag)
            if self.IS_DEBUG: print("[HashtagClassifier] _score: ", _score)
            _redefined = self.redefineEmotion(_score)
            if self.IS_DEBUG: print("[HashtagClassifier] _redefined: ", _redefined)
            score = self.sumScore(score, _redefined)
            if self.IS_DEBUG: print("[HashtagClassifier] score: ", score)

        if self.IS_DEBUG: print('------------------------------------------')
        return score

    def getHashtagScore(self, hashtag):
        score = {}
        vocabs = np.array(self.vocabDf["Word"])
        emotions = np.array(self.vocabDf["Emotion"])

        _index = vocabs.searchsorted(hashtag)
        if _index < len(emotions):
            emotion = emotions[_index]

            if self.IS_DEBUG: print("Emotion: ", emotion)

            if emotion in score:
                score[emotion] += 1
            else:
                score[emotion] = 1

            return score
        else:
            return score

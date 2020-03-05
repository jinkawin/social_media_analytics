import numpy as np
import pandas as pd

from django.conf import settings

from .NrcProcess import NrcProcess

class HashtagClassifier(NrcProcess):

    def __init__(self):
        super().__init__()

    def classify(self, hashtags):
        score = {}
        for hashtag in hashtags:
            # print("hashtag: ", hashtag)

            # score = self.getNrcScore(hashtag)

            # If there is no such a word in NRC lexicon, let's try in hashtag lexicon
            # if not score:
            score = self.getHashtagScore(hashtag, score)

        score = self.redefineEmotion(score)

        return score

    def getHashtagScore(self, hashtag, score):
        vocabs = np.array(self.vocabDf["Word"])
        emotions = np.array(self.vocabDf["Emotion"])

        _index = vocabs.searchsorted(hashtag)
        if _index < len(emotions):
            emotion = emotions[_index]

            # print("Emotion: ", emotion)

            if emotion in score:
                score[emotion] += 1
            else:
                score[emotion] = 1

            return score
        else:
            return score

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
            print("hashtag: ", hashtag)
            score = self.getNrcScore(hashtag)

            # If there is no such a word in NRC lexicon, let's try in hashtag lexicon
            # if not score:

            print("----------------------------------------")

        return score

    def getScore(self, hashtag):
        vocabs = np.array(self.vocabDf["Word"])
        emotions = np.array(self.vocabDf["Emotion"])
        # _index = vocabs.searchsorted(word)

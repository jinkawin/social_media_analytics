from django.conf import settings

import numpy as np
import pandas as pd

from .TextClassifier import TextClassifier

class HashtagClassifier:

    def __init__(self):
        self.vocabDf = self._readNrcLexiconFile('NRC_lexicon.csv')
        self.hashtagDf = self._readHashtagFile('NRC_hashtag_lexicon.txt')
        self.words = np.array(self.vocabDf["Word"])

    def classify(self, hashtags):
        score = {}
        for hashtag in hashtags:
            print("hashtag: ", hashtag)
            score = TextClassifier().getScore(hashtag)

            # If there is no such a word in NRC lexicon, let's try in hashtag lexicon
            # if not score:

            print("----------------------------------------")

        return score

    def _readNrcLexiconFile(self, filename):
        vocabDf = pd.read_csv(settings.STATIC_DIR + '/' + filename, encoding = "ISO-8859-1")
        vocabDf = vocabDf.sort_values(by="Word")
        return vocabDf

    def _readHashtagFile(self, filename):
        hashtagDf = pd.read_csv(settings.STATIC_DIR + '/' + filename, sep="	", names=["Emotion", "Word", "Score"])
        hashtagDf["Word"] = hashtagDf["Word"].replace({'#':''}, regex=True)
        hashtagDf = hashtagDf.sort_values(by="Word")

        return hashtagDf

    def printDict(self, dict):
        for key, value in dict.items():
            print("Key: ", key, "Value: ", value)

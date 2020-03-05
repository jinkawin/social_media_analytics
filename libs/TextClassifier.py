from django.conf import settings

import numpy as np
import pandas as pd

class TextClassifier:

    def __init__(self):
        self.vocabDf = self._readFile('NRC_lexicon.csv')
        self.words = np.array(self.vocabDf["Word"])

    def classify(self, text):
        score = {}
        for word in text:
            print("word: ", word)
            score = self._sumScore(word, score)
            print("score: ", score)
            print("------------------------------------")

        return score

    def getScore(self, word):
        vocabs = np.array(self.vocabDf["Word"])
        emotions = np.array(self.vocabDf["Emotion"])

        # Search the given word
        _index = vocabs.searchsorted(word)
        _nrcScore = {}

        # If there are many indices (one word has many emotion)
        while _index < len(vocabs) and vocabs[_index] == word:

            # init found emotions
            _nrcScore[emotions[_index]] = 1

            # move to the next index
            _index += 1

        print("_nrcScore: ")
        self.printDict(_nrcScore)
        nrcScore = self._redefineEmotion(_nrcScore)
        print("Redefine Emotion: ")
        self.printDict(nrcScore)

        return nrcScore


    def _sumScore(self, target, score):
        _score = self.getScore(target)

        # sum 2 dict up
        result = {key: score.get(key, 0) + _score.get(key, 0) for key in set(score) | set(_score)}
        print("result: ")
        self.printDict(result)

        return result

    def _readFile(self, filename):
        vocabDf = pd.read_csv(settings.STATIC_DIR + '/' + filename, encoding = "ISO-8859-1")
        vocabDf = vocabDf.sort_values(by="Word")
        return vocabDf

    def _redefineEmotion(self, score):
        # Exitement = trust
        # Happy = joy
        # Pleasant = positive
        # Surprise = negative, sadness, surprise
        # Fear = fear, disgust
        # Angry = anger

        result = {}

        if 'trust' in score:
            result['excitement'] = 1
        if 'joy' in score:
            result['happy'] = 1
        if 'positive' in score:
            result['pleasant'] = 1
        if 'negative' in score or 'sadness' in score or 'surprise' in score:
            result['surprise'] = 1
        if 'fear' in score or 'disgust' in score:
            result['fear'] = 1
        if 'anger' in score:
            result['angry'] = 1

        return result

    def printDict(self, dict):
        for key, value in dict.items():
            print("Key: ", key, "Value: ", value)


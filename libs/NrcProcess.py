import numpy as np
import pandas as pd

from django.conf import settings

class NrcProcess:

    def __init__(self):
        self.vocabDf = self._readNrcLexiconFile('NRC_lexicon.csv')
        self.hashtagDf = self._readHashtagFile('NRC_hashtag_lexicon.txt')
        self.words = np.array(self.vocabDf["Word"])

    def getNrcScore(self, word):
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
        nrcScore = self.redefineEmotion(_nrcScore)
        print("Redefine Emotion: ")
        self.printDict(nrcScore)

        return nrcScore

    def redefineEmotion(self, score):
        # Exitement = anticipation
        # Happy = joy
        # Pleasant = positive, trust
        # Surprise = negative, sadness, surprise
        # Fear = fear, disgust
        # Angry = anger

        result = {}

        if 'anticip' in score:
            result['excitement'] = 1
        if 'joy' in score:
            result['happy'] = 1
        if 'positive' in score or 'trust' in score:
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

    def _readNrcLexiconFile(self, filename):
        vocabDf = pd.read_csv(settings.STATIC_DIR + '/' + filename, encoding = "ISO-8859-1")
        vocabDf = vocabDf.sort_values(by="Word")
        return vocabDf

    def _readHashtagFile(self, filename):
        hashtagDf = pd.read_csv(settings.STATIC_DIR + '/' + filename, sep="	", names=["Emotion", "Word", "Score"])
        hashtagDf["Word"] = hashtagDf["Word"].replace({'#':''}, regex=True)
        hashtagDf = hashtagDf.sort_values(by="Word")

        return hashtagDf
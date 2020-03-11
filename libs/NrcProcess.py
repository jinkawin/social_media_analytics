import numpy as np
import pandas as pd

from django.conf import settings
from libs.emotions.EmotionEnum import EmotionEnum

class NrcProcess:
    IS_DEBUG = False

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

        nrcScore = self.redefineEmotion(_nrcScore)
        # nrcScore = _nrcScore

        return nrcScore

    def redefineEmotion(self, score):
        result = self._initEmotionScore()

        # [Version 1]
        # Exitement = anticipation
        # Happy = joy
        # Pleasant = positive, trust
        # Surprise = negative, sadness, surprise
        # Fear = fear, disgust
        # Angry = anger

        # if 'anticip' in score:
        #     result[EmotionEnum.EXCITEMENT.value.NAME] = 1
        # if 'joy' in score:
        #     result[EmotionEnum.HAPPY.value.NAME] = 1
        # if 'positive' in score or 'trust' in score:
        #     result[EmotionEnum.PLEASANT.value.NAME] = 1
        # if 'negative' in score or 'sadness' in score or 'surprise' in scor e:
        #     result[EmotionEnum.SURPRISE.value.NAME] = 1
        # if 'fear' in score or 'disgust' in score:
        #     result[EmotionEnum.FEAR.value.NAME] = 1
        # if 'anger' in score:
        #     result[EmotionEnum.ANGRY.value.NAME] = 1

        # -------------------------------------------------------------------

        # [Version 2]
        # Positive
        # Exitement = positive + anticipation, positive + surprise
        # Happy = positive + joy, positive + fear, positive + sadness
        # Pleasant = positive + trust, positive + anger, positive + disgust

        # Negative
        # Surprise = negative + sadness, negative + surprise, negative + joy
        # Fear = negative + fear, negative + anticipation, negative + trust
        # Angry = negative + anger, negative + disgust

        # Neutral
        # Exitement = anticipation
        # Happy = joy
        # Pleasant = trust
        # Surprise = sadness, surprise
        # Fear = fear
        # Angry = anger, disgust

        # Positive
        if 'positive' in score:
            if 'anticip' in score or 'surprise' in score:
                result[EmotionEnum.EXCITEMENT.value.NAME] += 1
            if 'joy' in score or 'fear' in score or 'sadness' in score:
                result[EmotionEnum.HAPPY.value.NAME] += 1
            if 'trust' in score or 'anger' in score or 'disgust' in score:
                result[EmotionEnum.PLEASANT.value.NAME] += 1

        # Negative
        elif 'negative' in score:
            if 'sadness' in score or 'surprise' in score or 'joy' in score:
                result[EmotionEnum.SURPRISE.value.NAME] += 1
            if 'anticip' in score or 'fear' in score or 'trust' in score:
                result[EmotionEnum.FEAR.value.NAME] += 1
            if 'anger' in score or 'disgust' in score:
                result[EmotionEnum.ANGRY.value.NAME] += 1


        # Neutral
        else:
            if 'anticip' in score:
                result[EmotionEnum.EXCITEMENT.value.NAME] += 1
            if 'joy' in score:
                result[EmotionEnum.HAPPY.value.NAME] += 1
            if 'trust' in score:
                result[EmotionEnum.PLEASANT.value.NAME] += 1
            if 'sadness' in score or 'surprise' in score:
                result[EmotionEnum.SURPRISE.value.NAME] += 1
            if 'fear' in score:
                result[EmotionEnum.FEAR.value.NAME] += 1
            if 'anger' in score or 'disgust' in score:
                result[EmotionEnum.ANGRY.value.NAME] += 1

        return result

    def printDict(self, dict):
        for key, value in dict.items():
            print("Key: ", key, ", Value: ", value)

    def _readNrcLexiconFile(self, filename):
        vocabDf = pd.read_csv(settings.STATIC_DIR + '/' + filename, encoding = "ISO-8859-1")
        vocabDf = vocabDf.sort_values(by="Word")
        return vocabDf

    def _readHashtagFile(self, filename):
        hashtagDf = pd.read_csv(settings.STATIC_DIR + '/' + filename, sep="	", names=["Emotion", "Word", "Score"])
        hashtagDf["Word"] = hashtagDf["Word"].replace({'#':''}, regex=True)
        hashtagDf = hashtagDf.sort_values(by="Word")

        return hashtagDf

    def _initEmotionScore(self):
        score = {}
        for emotionEnum in EmotionEnum:
            score[emotionEnum.value.NAME] = 0

        return score

    def sumScore(self, score1, score2):
        # sum 2 dict up
        result = {key: score1.get(key, 0) + score2.get(key, 0) for key in set(score1) | set(score2)}
        if self.IS_DEBUG: print("[NrcProcess] result: ", result)

        return result

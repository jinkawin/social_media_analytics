from .TextClassifier import TextClassifier
from .HashtagClassifier import HashtagClassifier
from .EmoticonClassifier import EmoticonClassifier
from .NrcProcess import NrcProcess

class Classifier:
    IS_DEBUG = False

    def __init__(self):
        self.textClassifier = TextClassifier()
        self.hashtagClassifier = HashtagClassifier()
        self.emoticonClassifier = EmoticonClassifier()
        self.nrcProcess = NrcProcess()

    def classify(self, tweets, emotionClass):
        classifierAnalysis = {}
        scoreAnalysis = {}
        score = {}
        result = {}

        for tweet in tweets:
            text = tweet.getProcessedText()
            hashtag = tweet.getHashtag()
            fullText = tweet.getFullText()

            if self.IS_DEBUG: print("[Classifier] Full Text: ", fullText)

            _score = self.textClassifier.classify(text)
            score = self.nrcProcess.sumScore(_score, score)

            if self.IS_DEBUG: print("[Classifier] nrcProcess: ", score)

            _score = self.hashtagClassifier.classify(hashtag)
            score = self.nrcProcess.sumScore(_score, score)

            _score = self.emoticonClassifier.classify(fullText)
            # If there is emoticon in the tweet
            if _score:
                tweet.setIsContainEmoticon(True)
            score = self.nrcProcess.sumScore(_score, score)

            if self.IS_DEBUG: print("[Classifier] Score: ", score)

            if score:
                # Find the max score
                maxScore = max(sorted(score.values()))
                maxValues = [k for k,v in score.items() if v == maxScore]

                # For Analysis
                if self.IS_DEBUG: print("[Classifier] Max Value: ", maxValues)
                if self.IS_DEBUG: print("[Classifier] emotionClass: ", emotionClass)
                for value in maxValues:
                    if value in scoreAnalysis:
                        scoreAnalysis[value] += 1
                    else:
                        scoreAnalysis[value] = 1

                if len(maxValues) == 1:
                    _classified = maxValues[0]
                    # If the classified tweet is the same as given class
                    if _classified == emotionClass:
                        result[tweet.getId()] = tweet

                    # For Analysis
                    if _classified in classifierAnalysis:
                        classifierAnalysis[_classified] += 1
                    else:
                        classifierAnalysis[_classified] = 1

                # reset the score
                score = {}
                if self.IS_DEBUG: print("[Classifier] ===================================")
            # END If
        # END For

        # For Analysis
        if self.IS_DEBUG: print("[Classifier] scoreAnalysis: ", scoreAnalysis)
        if self.IS_DEBUG: print("[Classifier] classifierAnalysis: ", classifierAnalysis)

        return result
from .TextClassifier import TextClassifier
from .HashtagClassifier import HashtagClassifier
from .EmoticonClassifier import EmoticonClassifier
from .NrcProcess import NrcProcess

class Classifier:
    def __init__(self):
        self.textClassifier = TextClassifier()
        self.hashtagClassifier = HashtagClassifier()
        self.emoticonClassifier = EmoticonClassifier()
        self.nrcProcess = NrcProcess()

    def classify(self, tweets):
        classifierAnalysis = {}
        scoreAnalysis = {}
        score = {}

        for tweet in tweets:
            text = tweet.getProcessedText()
            hashtag = tweet.getHashtag()
            fullText = tweet.getFullText()

            print("Full Text: ", fullText)

            _score = self.textClassifier.classify(text)
            score = self.nrcProcess.sumScore(_score, score)
            _score = self.hashtagClassifier.classify(hashtag)
            score = self.nrcProcess.sumScore(_score, score)
            _score = self.emoticonClassifier.classify(fullText)
            score = self.nrcProcess.sumScore(_score, score)

            # Find the max score
            maxScore = max(sorted(score.values()))
            maxValues = [k for k,v in score.items() if v == maxScore]

            print("Value: ", maxValues)
            for value in maxValues:
                if value in scoreAnalysis:
                    scoreAnalysis[value] += 1
                else:
                    scoreAnalysis[value] = 1

            if len(maxValues) == 1:
                _classified = maxValues[0]
                if _classified in classifierAnalysis:
                    classifierAnalysis[_classified] += 1
                else:
                    classifierAnalysis[_classified] = 1

            # for item in maxValues:
            #     print("maxValues: ", item)
            # reset the score
            score = {}
            print("===================================")
        # END For

        print("scoreAnalysis: ", scoreAnalysis)
        print("classifierAnalysis: ", classifierAnalysis)

from .TextClassifier import TextClassifier
from .HashtagClassifier import HashtagClassifier

class Classifier:
    def __init__(self):
        self.textClassifier = TextClassifier()
        self.hashtagClassifier = HashtagClassifier()

    def classify(self, tweets):
        score = {}

        for tweet in tweets:
            text = tweet.getProcessedText()
            hashtag = tweet.getHashtag()

            # print("Original", tweet.getFullText())

            # score = self.textClassifier.classify(text)
            self.hashtagClassifier.classify(hashtag)


            # Find the max score
            # maxScore = max(sorted(score.values()))
            # maxValues = [k for k,v in score.items() if v == maxScore]

            # for item in maxValues:
            #     print("maxValues: ", item)
            # reset the score
            score = {}
            print("===================================")
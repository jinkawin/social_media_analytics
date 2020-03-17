from libs.emotions.Emotion import Emotion
from data_crawler.models import FearModel
from data_crawler.models import FearSampleModel

class Fear(Emotion):
    NAME = 'Fear'
    HASHTAGS = ['#fear', '#horror', '#depressed']
    EMOTICONS = ["D‑':", 'D:', 'D;', 'DX', 'D=']

    def __init__(self):
        super().__init__(self.HASHTAGS, self.EMOTICONS)

    def getDB(self):
        return FearModel

    def getSampleDB(self):
        return FearSampleModel

    def hello(self):
        print("Fear")
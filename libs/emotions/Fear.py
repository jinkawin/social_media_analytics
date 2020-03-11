from libs.emotions.Emotion import Emotion
from data_crawler.models import FearModel

class Fear(Emotion):
    NAME = 'Fear'
    HASHTAGS = ['#fear', '#horror', '#depressed']
    EMOTICONS = ["D‑':", 'D:', 'D;', 'DX', 'D=']

    def __init__(self):
        super().__init__(self.HASHTAGS, self.EMOTICONS)

    def getDB(self):
        return FearModel

    def hello(self):
        print("Fear")
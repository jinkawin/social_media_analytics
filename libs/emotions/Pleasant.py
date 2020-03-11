from libs.emotions.Emotion import Emotion
from data_crawler.models import PleasantModel

class Pleasant(Emotion):
    NAME = 'Pleasant'
    HASHTAGS = ['#pleasant', '#accept', '#agreed', '#hire', '#dope', '#awesome', '#superb']
    EMOTICONS = [':3']

    def __init__(self):
        super().__init__(self.HASHTAGS, self.EMOTICONS)

    def getDB(self):
        return PleasantModel

    def hello(self):
        print("Pleasant")
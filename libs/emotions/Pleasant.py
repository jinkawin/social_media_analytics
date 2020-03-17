from libs.emotions.Emotion import Emotion
from data_crawler.models import PleasantModel
from data_crawler.models import PleasantSampleModel

class Pleasant(Emotion):
    NAME = 'Pleasant'
    HASHTAGS = ['#pleasant', '#accept', '#agreed', '#hire', '#dope', '#awesome', '#superb']
    EMOTICONS = [':3']

    def __init__(self):
        super().__init__(self.HASHTAGS, self.EMOTICONS)

    def getDB(self):
        return PleasantModel

    def getSampleDB(self):
        return PleasantSampleModel

    def hello(self):
        print("Pleasant")
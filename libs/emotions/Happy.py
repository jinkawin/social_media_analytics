from libs.emotions.Emotion import Emotion
from data_crawler.models import HappyModel
from data_crawler.models import HappySampleModel

class Happy(Emotion):
    NAME = 'Happy'
    HASHTAGS = ['#beach', '#happy', '#joy']
    EMOTICONS = [':)', ';)', ':]', ';]', ':P', ';P', ':D', ';D', ':>', ':-)', ';-)', ':^)', ';^)', ':-D', ':->', '=)', '=]', '<3']

    def __init__(self):
        super().__init__(self.HASHTAGS, self.EMOTICONS)

    def getDB(self):
        return HappyModel

    def getSampleDB(self):
        return HappySampleModel

    def hello(self):
        print("Happy")
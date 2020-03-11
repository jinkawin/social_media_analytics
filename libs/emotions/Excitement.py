from libs.emotions.Emotion import Emotion
from data_crawler.models import ExcitementModel

class Excitement(Emotion):
    NAME = 'Excitement'
    HASHTAGS = ['#excitement', '#adventure', '#motivation', '#passion']
    EMOTICONS = ['o_O', 'O_o', 'o.O', 'O.o', 'o_0', '0_o']

    def __init__(self):
        super().__init__(self.HASHTAGS, self.EMOTICONS)

    def getDB(self):
        return ExcitementModel

    def hello(self):
        print("Excitement")
from libs.emotions.Emotion import Emotion
from data_crawler.models import AngryModel

class Angry(Emotion):
    NAME = 'Angry'
    HASHTAGS = ['#angry', '#shutup', '#arguments', '#mad', '#pissoff', '#racist']
    EMOTICONS = [':@', '>:(', '>:[', ':/', ':‑/', '=/', ':S']

    def __init__(self):
        super().__init__(self.HASHTAGS, self.EMOTICONS)

    def getDB(self):
        return AngryModel

    def hello(self):
        print("Angry")

from libs.emotions.Emotion import Emotion
from data_crawler.models import SurpriseModel

class Surprise(Emotion):
    NAME = 'Surprise'
    HASHTAGS = ['#surprise', '#cry', '#sad']
    EMOTICONS = [':‑(', ':(', ':c', ':‑c', ':<', ':‑<', ':[', ':‑[', ':-||', ":'(", ":'‑(", ':O', ':‑O', ':o', ':‑o', ':-0']

    def __init__(self):
        super().__init__(self.HASHTAGS, self.EMOTICONS)

    def getDB(self):
        return SurpriseModel

    def hello(self):
        return "Surprise"
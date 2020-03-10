from libs.emotions.Emotion import Emotion

class Surprise(Emotion):
    NAME = 'Surprise'
    HASHTAGS = ['#surprise', '#cry', '#sad']
    EMOTICONS = [':‑(', ':(', ':c', ':‑c', ':<', ':‑<', ':[', ':‑[', ':-||', ":'(", ":'‑(", ':O', ':‑O', ':o', ':‑o', ':-0']

    def __init__(self):
        super().__init__(self.HASHTAGS, self.EMOTICONS)

    def hello(self):
        return "Surprise"
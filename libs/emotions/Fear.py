from libs.emotions.Emotion import Emotion

class Fear(Emotion):
    HASHTAGS = ['fear', 'horror', 'depressed']
    EMOTICONS = ["D‑':", 'D:', 'D;', 'DX', 'D=']

    def __init__(self):
        super().__init__(self.HASHTAGS, self.EMOTICONS)

    def hello(self):
        return "Fear"
from libs.emotions.Emotion import Emotion

class Pleasant(Emotion):
    HASHTAGS = ['pleasant', 'accept', 'attractive']
    EMOTICONS = [':3']

    def __init__(self):
        super().__init__(self.HASHTAGS, self.EMOTICONS)

    def hello(self):
        return "Pleasant"
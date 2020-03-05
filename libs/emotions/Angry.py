from libs.emotions.Emotion import Emotion

class Angry(Emotion):
    HASHTAGS = ['angry', 'annoyed', 'hate', 'irritated']
    EMOTICONS = [':@', '>:(', '>:[', ':/', ':‑/', '=/', ':S']

    def __init__(self):
        super().__init__(self.HASHTAGS, self.EMOTICONS)

    def hello(self):
        return "Angry"
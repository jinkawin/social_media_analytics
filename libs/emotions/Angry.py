from libs.emotions.Emotion import Emotion

class Angry(Emotion):
    NAME = 'Angry'
    # HASHTAGS = ['#angry', '#annoyed', '#hate', '#irritated', '#shutup', '#damn', '#mad', '#pissoff', '#racist']
    HASHTAGS = ['#arguments']
    EMOTICONS = [':@', '>:(', '>:[', ':/', ':‑/', '=/', ':S']

    def __init__(self):
        super().__init__(self.HASHTAGS, self.EMOTICONS)

    def hello(self):
        print("Angry")
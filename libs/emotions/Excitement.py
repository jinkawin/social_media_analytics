from libs.emotions.Emotion import Emotion

class Excitement(Emotion):
    NAME = 'Excitement'
    HASHTAGS = ['#excitement', '#adventure', '#motivation', '#passion']
    EMOTICONS = ['o_O', 'O_o', 'o.O', 'O.o', 'o_0', '0_o']

    def __init__(self):
        super().__init__(self.HASHTAGS, self.EMOTICONS)

    def hello(self):
        print("Excitement")
from libs.emotions.Emotion import Emotion

class Happy(Emotion):

    def __init__(self):
        super().__init__("happy")

    def hello(self):
        return super().hello()
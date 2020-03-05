from libs.emotions.Emotion import Emotion

class Happy(Emotion):
    HASHTAGS = ['happy', 'love', 'joy']
    EMOTICONS = [':)', ';)', ':]', ';]', ':P', ';P', ':D', ';D', ':>', ':-)', ';-)', ':^)', ';^)', ':-D', ':->', '=)', '=]', '<3']

    def __init__(self):
        super().__init__(self.HASHTAGS, self.EMOTICONS)

    def hello(self):
        print("hello")
        # return super().hello()
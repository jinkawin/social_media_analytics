class Emotion:

    def __init__(self, hashtags, emoticons):
        self.hashtag = hashtags
        self.emoticons = emoticons

    def getHashtags(self):
        return self.hashtag

    def getEmoticons(self):
        return self.emoticons

    def hello(self):
        return "Emotion"
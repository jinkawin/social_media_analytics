class Tweet:
    FIRST_INDEX = 0
    LAST_INDEX = 1

    def __init__(self, tweetObj):
        self.tweet = tweetObj
        self.id = tweetObj.id_str
        self.fullText = tweetObj.full_text

        self.text, self.hashtag = self._normalise(tweetObj)

    def getTweet(self):
        return self.tweet

    def getId(self):
        return self.id

    def getFullText(self):
        return self.fullText

    def getText(self):
        print('self.text', self.text)
        return self.text

    def getHashtag(self):
        print('self.hashtag', self.hashtag)
        return self.hashtag

    def _normalise(self, tweet):
        _text = ''
        _hashtagList = list()

        hashtags = tweet.entities['hashtags']
        tweetLength = len(tweet.full_text)

        # If hashtag is not in the end of the tweet, convert all hashtag to normal text
        if(hashtags[len(hashtags)-1]['indices'][self.LAST_INDEX] != tweetLength):
            _text = self._removeAllHashtag(tweet.full_text)
        else:
        # If it is not, extract hashtag, which are in the end of the tweet,
        # and remove all hashtags that are in middle of the tweet
            _hashtagList, lastIndex = self._extractHashTag(tweetLength, hashtags)
            _text = self._removeAllHashtag(tweet.full_text[:lastIndex])

        return (_text, _hashtagList)

    # Convert from hashtag to normal text
    def _removeAllHashtag(self, tweet):
        return tweet.replace('#', '')

    # Get hashtag from the tweet
    # {'text': 'goodhusband', 'indices': [239, 251]}, {'text': 'comedygreats', 'indices': [252, 265]}
    def _extractHashTag(self, tweetLength, hashtags):
        result = list()

        checkIndex = tweetLength
        for i in range(len(hashtags), 0, -1):

            # Check whether hashtag is in the end of the tweet
            if(hashtags[i-1]['indices'][self.LAST_INDEX] == checkIndex):
                result.append(hashtags[i-1]['text'])
                checkIndex = hashtags[i-1]['indices'][self.FIRST_INDEX] - 1
            else:
                break

        return (result, checkIndex)
import tweepy
from libs.Tweet import Tweet

class TwitterCrawler:

    MAX_TWEETS = 5

    def __init__(self):
        self.consumer_key = '9Wc1trOeRGpo6PvPOUMPwUDWK'
        self.consumer_secret = 'T4v7tw8lhxYP6E6IDrSnIAnzxgqrgrvtJI4vMdEVnWf3ZXDi8d'
        self.access_token = '300137857-TGWENhyaddCnmG8DS9dsAu7PgruX4bNITxacvoJz'
        self.access_token_secret = 'Q0441ZZDAVBbDiiU0zK0zYBuIOkaryx3MpapEmOFD2Cm5'
        self.auth, self.api = self._auth()

    # Authentication by keys
    def _auth(self):
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)

        api = tweepy.API(auth)
        return (auth, api)

    # Search tweet by query
    def searchTweet(self, query, langs):
        result = list()

        # extended_mode is getting full text
        searched_tweets = [status for status in tweepy.Cursor(self.api.search, q=query, tweet_mode='extended', lang='en').items(self.MAX_TWEETS)]

        for tweet in searched_tweets:
            result.append(Tweet(tweet))

        return result
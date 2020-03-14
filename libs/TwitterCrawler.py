import tweepy

from libs.Tweet import Tweet
from libs.DataProcessor import DataProcessor
from libs.Classifier import Classifier

class TwitterCrawler:

    MAX_TWEETS = 150

    def __init__(self):
        self.consumer_key = '9Wc1trOeRGpo6PvPOUMPwUDWK'
        self.consumer_secret = 'T4v7tw8lhxYP6E6IDrSnIAnzxgqrgrvtJI4vMdEVnWf3ZXDi8d'
        self.access_token = '300137857-TGWENhyaddCnmG8DS9dsAu7PgruX4bNITxacvoJz'
        self.access_token_secret = 'Q0441ZZDAVBbDiiU0zK0zYBuIOkaryx3MpapEmOFD2Cm5'
        self.auth, self.api = self._auth()


        self.dataProcessor = DataProcessor()
        self.classifier = Classifier()

    # Authentication by keys
    def _auth(self):
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)

        api = tweepy.API(auth)
        return (auth, api)

    # Search tweet by query
    def searchTweet(self, query, langs, emotionClass):
        result = {}

        # extended_mode is getting full text
        i = 0
        for page in tweepy.Cursor(self.api.search, q=query, tweet_mode='extended', lang='en', rpp=100).pages():
            print("Fetching a new page... ", i)
            print("There are ", len(page), ' tweets')
            _classified = self._pageProcess(page, emotionClass)
            print("Count classified: ", len(_classified))
            result = {**result, **_classified}
            i += 1

            print("Total: ", len(result))
            if(len(result) >= self.MAX_TWEETS):
                break


        print("---------------- ", emotionClass, "Summary ----------------")
        print("Total number of crawled tweets: ", i * 15)
        print("Total number of classified tweets: ", len(result))
        print("Total number of removed tweets: ", (i*15) - len(result))
        print("---------------- /Summary ----------------")
        return result

    def _pageProcess(self, page, emotionClass):
        tweetContainer = list()
        classified = list()

        for tweet in page:
            _tweet = Tweet(tweet)

            # Pre-process
            _tweet.setProcessedText(self.dataProcessor.preProcess(_tweet.getText()))

            # Classify
            tweetContainer.append(_tweet)

        classified = self.classifier.classify(tweetContainer, emotionClass)
        return classified
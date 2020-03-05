from django.shortcuts import render
from libs.TwitterCrawler import TwitterCrawler
from libs.DataProcessor import DataProcessor
from libs.Classifier import Classifier
from libs.HashtagClassifier import HashtagClassifier

from libs.emotions.EmotionEnum import EmotionEnum

from data_crawler.models import Tweet

def index(request):

    context_dict = {}

# TODO: Crawl others 5 classes
# # Twiiter crawler
#     # Init
#     twitterCrawler = TwitterCrawler()

#     # Twitter Crawler
#     tweets = twitterCrawler.searchTweet('#happy -filter:retweets -filter:links', 'en')

# # Pre-process
#     processedTweets = list()
#     dataProcessor = DataProcessor()

#     for tweet in tweets:
#         tweet.setProcessedText(dataProcessor.preProcess(tweet.getText()))

# # # Classifier
    # classifier = Classifier()
    # classifier.classify(tweets)

    hashtagClassifier = HashtagClassifier()


# MongoDB
    # Save to MongoDB
    # try:
    #     tweets = Tweet.objects.all()
    #     for tweet in tweets:
    #         print(tweet.name)
    # except Tweet.DoesNotExist:
    #     print('None')

    # tweet = Tweet(name='Win')
    # tweet.name = 'Jinkawin'
    # tweet.save()

    # context_dict['tweets'] = tweets
    # context_dict['processedTweets'] = processedTweets
    response = render(request, 'data_crawler/index.html', context = context_dict)
    return response
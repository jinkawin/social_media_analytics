from django.shortcuts import render
from libs.TwitterCrawler import TwitterCrawler
from libs.DataProcessor import DataProcessor

from libs.emotions.Happy import Happy

from data_crawler.models import Tweet

def index(request):

    context_dict = {}
    data = {}

# Twiiter crawler
    # Init
    twitterCrawler = TwitterCrawler()

    # Twitter Crawler
    tweets = twitterCrawler.searchTweet('#happy -filter:retweets -filter:links', 'en')

# Pre-process
    processedTweets = list()
    dataProcessor = DataProcessor()

    for tweet in tweets:
        tweet.setProcessedText(dataProcessor.preProcess(tweet.getText()))

    # dataProcessor.preProcess("Hello!, I am won't haven't can't loove you :)  #happy #test")
    # _temp = dataProcessor.preProcess("Heeellooo, I am #happy. Looooove you guys ;)")
    # print(_temp)

# Classifier


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

    context_dict['tweets'] = tweets
    context_dict['processedTweets'] = processedTweets
    response = render(request, 'data_crawler/index.html', context = context_dict)
    return response
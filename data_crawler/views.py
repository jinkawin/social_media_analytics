from datetime import datetime, timedelta

from django.shortcuts import render
from libs.TwitterCrawler import TwitterCrawler

from data_crawler.models import HappyModel
from data_crawler.models import FearModel
from data_crawler.models import AngryModel
from data_crawler.models import SurpriseModel
from data_crawler.models import ExcitementModel
from data_crawler.models import PleasantModel

from libs.emotions.EmotionEnum import EmotionEnum
from libs.EmoticonClassifier import EmoticonClassifier

from random import shuffle
import csv

def index(request):

    context_dict = {}

    # twitterCrawler = TwitterCrawler()

    # seeds = ' OR '.join(EmotionEnum.PLEASANT.value.HASHTAGS)

    # tweets = twitterCrawler.searchTweet(seeds + ' -filter:retweets -filter:links', 'en', EmotionEnum.PLEASANT.value.NAME)

    # MongoDB
    # for _id, tweet in tweets.items():
    #     tweetModel = PleasantModel()
    #     tweetModel.tweet_id = tweet.getId()
    #     tweetModel.original_text = tweet.getFullText()
    #     tweetModel.processed_text = tweet.getProcessedText()
    #     tweetModel.is_contain_emoticon = tweet.getIsContainEmoticon()
    #     tweetModel.create_at = tweet.getCreateAt()
    #     tweetModel.save()

    # context_dict['tweets'] = tweets
    # context_dict['processedTweets'] = processedTweets
    response = render(request, 'data_crawler/index.html', context = context_dict)
    return response

def generateCsv(request):
    context_dict = {}
    records = []

    for emotion in EmotionEnum:
        _list = []
        db = emotion.value.getDB()
        tweets = db.objects.all()
        # _list = list(tweets.values())
        _list = [[tweet['original_text'].encode('ascii', 'ignore').decode('ascii'), emotion.value.NAME] for tweet in tweets.values()]
        records += _list[:20]

    shuffle(records)
    writeCsv(records)
    response = render(request, 'data_crawler/index.html', context = context_dict)
    return response

def writeCsv(records):
    # http://zetcode.com/python/csv/

    f = open('result.csv', 'w')

    with f:
        writer = csv.writer(f)
        writer.writerow(['text'])

        for record in records:
            writer.writerow(record)
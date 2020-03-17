import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'social_media_analytics.settings')
django.setup()

from datetime import datetime, timedelta
from django.shortcuts import render

from data_crawler.models import HappyModel
from data_crawler.models import FearModel
from data_crawler.models import AngryModel
from data_crawler.models import SurpriseModel
from data_crawler.models import ExcitementModel
from data_crawler.models import PleasantModel

from libs.emotions.EmotionEnum import EmotionEnum
from libs.EmoticonClassifier import EmoticonClassifier
from libs.TwitterCrawler import TwitterCrawler

from random import shuffle
import csv
import tweepy
import json

context_dict = {}

twitterCrawler = TwitterCrawler()

test = {'full_text': 'Jinkawin'}
_test = json.dumps(test)
print(_test)

# for emotion in EmotionEnum:

#     seeds = ' OR '.join(emotion.value.HASHTAGS)
#     query = seeds + ' -filter:retweets -filter:links'

#     twitterCrawler = TwitterCrawler()

#     searched_tweets = [tweet for tweet in tweepy.Cursor(twitterCrawler.api.search, q=query, tweet_mode='extended', lang='en').items(10)]
#     # writeCsv(searched_tweets)

#     for tweet in searched_tweets:
#         print(tweet)

def writeCsv(records):
    # http://zetcode.com/python/csv/

    with f:
        writer = csv.writer(f)
        writer.writerow(['text'])

        for record in records:
            writer.writerow(record)
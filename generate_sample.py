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

from types import SimpleNamespace

# context_dict = {'key1': 'value1', 'key2': 'value2'}
# n = SimpleNamespace(**context_dict)

def _auth():
    consumer_key = '9Wc1trOeRGpo6PvPOUMPwUDWK'
    consumer_secret = 'T4v7tw8lhxYP6E6IDrSnIAnzxgqrgrvtJI4vMdEVnWf3ZXDi8d'
    access_token = '300137857-TGWENhyaddCnmG8DS9dsAu7PgruX4bNITxacvoJz'
    access_token_secret = 'Q0441ZZDAVBbDiiU0zK0zYBuIOkaryx3MpapEmOFD2Cm5'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    return (auth, api)

def searchTweet(query):
    result = {}
    auth, api = _auth()

    return [tweet for tweet in tweepy.Cursor(api.search, q=query, tweet_mode='extended', lang='en').items(20)]

for emotion in EmotionEnum:

    seeds = ' OR '.join(EmotionEnum.HAPPY.value.HASHTAGS)
    tweets = searchTweet(seeds + ' -filter:retweets -filter:links')

    # MongoDB
    for tweet in tweets:
        model = emotion.value.getSampleDB()
        tweetModel = model()
        tweetModel.id_str = tweet.id_str
        tweetModel.full_text = tweet.full_text
        tweetModel.created_at = tweet.created_at
        tweetModel.save()

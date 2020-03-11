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

context_dict = {}

twitterCrawler = TwitterCrawler()

for emotion in EmotionEnum:

    seeds = ' OR '.join(emotion.value.HASHTAGS)
    tweets = twitterCrawler.searchTweet(seeds + ' -filter:retweets -filter:links', 'en', emotion.value.NAME)

    # MongoDB
    for _id, tweet in tweets.items():
        model = emotion.value.getDB()
        tweetModel = model()
        tweetModel.tweet_id = tweet.getId()
        tweetModel.original_text = tweet.getFullText()
        tweetModel.processed_text = tweet.getProcessedText()
        tweetModel.is_contain_emoticon = tweet.getIsContainEmoticon()
        tweetModel.create_at = tweet.getTweet().created_at
        tweetModel.save()
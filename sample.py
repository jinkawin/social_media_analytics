import os
import django
import csv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'social_media_analytics.settings')
django.setup()

from types import SimpleNamespace

from random import shuffle

from datetime import datetime, timedelta
from django.shortcuts import render

from data_crawler.models import HappyModel
from data_crawler.models import FearModel
from data_crawler.models import AngryModel
from data_crawler.models import SurpriseModel
from data_crawler.models import ExcitementModel
from data_crawler.models import PleasantModel
from data_crawler.models import HappySampleModel

from libs.emotions.EmotionEnum import EmotionEnum
from libs.EmoticonClassifier import EmoticonClassifier
from libs.TwitterCrawler import TwitterCrawler
from libs.DataProcessor import DataProcessor
from libs.Classifier import Classifier
from libs.Tweet import Tweet

def process(tweets, emotionClass):
    tweetContainer = list()
    classified = list()

    dataProcessor = DataProcessor()
    classifier = Classifier()

    for tweet in tweets:
        _tweet = Tweet(tweet)

    #     # Pre-process
    #     _tweet.setProcessedText(dataProcessor.preProcess(_tweet.getText()))

    #     # Classify
    #     tweetContainer.append(_tweet)

    # classified = classifier.classify(tweetContainer, emotionClass)
    return classified

tweets = HappySampleModel.objects.all()
result = process(tweets, EmotionEnum.HAPPY.value.NAME)


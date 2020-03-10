from datetime import datetime, timedelta

from django.shortcuts import render
from libs.TwitterCrawler import TwitterCrawler

from data_crawler.models import HappyModel

from libs.emotions.EmotionEnum import EmotionEnum
from libs.EmoticonClassifier import EmoticonClassifier

def index(request):

    context_dict = {}

    twitterCrawler = TwitterCrawler()

    seeds = ' OR '.join(EmotionEnum.HAPPY.value.HASHTAGS)

    tweets = twitterCrawler.searchTweet(seeds + ' -filter:retweets -filter:links', 'en', EmotionEnum.HAPPY.value.NAME)

    # MongoDB
    for _id, tweet in tweets.items():
        tweetModel = HappyModel()
        tweetModel.tweet_id = tweet.getId()
        tweetModel.original_text = tweet.getFullText()
        tweetModel.processed_text = tweet.getProcessedText()
        tweetModel.is_contain_emoticon = tweet.getIsContainEmoticon()
        tweetModel.create_at = tweet.getTweet().created_at
        tweetModel.save()

    # context_dict['tweets'] = tweets
    # context_dict['processedTweets'] = processedTweets
    response = render(request, 'data_crawler/index.html', context = context_dict)
    return response
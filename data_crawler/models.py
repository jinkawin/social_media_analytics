from django.db import models

class HappyModel(models.Model):
    tweet_id = models.CharField(max_length=50)
    original_text =  models.TextField()
    processed_text = models.TextField()
    is_contain_emoticon = models.BooleanField()
    create_at = models.CharField(max_length=50)

class SurpriseModel(models.Model):
    tweet_id = models.CharField(max_length=50)
    original_text =  models.TextField()
    processed_text = models.TextField()
    is_contain_emoticon = models.BooleanField()
    create_at = models.CharField(max_length=50)

class ExcitementModel(models.Model):
    tweet_id = models.CharField(max_length=50)
    original_text =  models.TextField()
    processed_text = models.TextField()
    is_contain_emoticon = models.BooleanField()
    create_at = models.CharField(max_length=50)

class FearModel(models.Model):
    tweet_id = models.CharField(max_length=50)
    original_text =  models.TextField()
    processed_text = models.TextField()
    is_contain_emoticon = models.BooleanField()
    create_at = models.CharField(max_length=50)

class AngryModel(models.Model):
    tweet_id = models.CharField(max_length=50)
    original_text =  models.TextField()
    processed_text = models.TextField()
    is_contain_emoticon = models.BooleanField()
    create_at = models.CharField(max_length=50)

class PleasantModel(models.Model):
    tweet_id = models.CharField(max_length=50)
    original_text =  models.TextField()
    processed_text = models.TextField()
    is_contain_emoticon = models.BooleanField()
    create_at = models.CharField(max_length=50)
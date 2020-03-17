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

class HappySampleModel(models.Model):
    id_str = models.CharField(max_length=50)
    full_text =  models.TextField()
    created_at = models.CharField(max_length=50)

class SurpriseSampleModel(models.Model):
    id_str = models.CharField(max_length=50)
    full_text =  models.TextField()
    created_at = models.CharField(max_length=50)

class ExcitementSampleModel(models.Model):
    id_str = models.CharField(max_length=50)
    full_text =  models.TextField()
    created_at = models.CharField(max_length=50)

class FearSampleModel(models.Model):
    id_str = models.CharField(max_length=50)
    full_text =  models.TextField()
    created_at = models.CharField(max_length=50)

class AngrySampleModel(models.Model):
    id_str = models.CharField(max_length=50)
    full_text =  models.TextField()
    created_at = models.CharField(max_length=50)

class PleasantSampleModel(models.Model):
    id_str = models.CharField(max_length=50)
    full_text =  models.TextField()
    created_at = models.CharField(max_length=50)

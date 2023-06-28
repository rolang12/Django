from django.db import models

# Create your models here.

class Person(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Article(models.Model):

    title = models.CharField(max_length=100)
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True) #crear la fecha automaticamente actual por primera vez
    upd_date = models.DateTimeField(auto_now=True) #crear la fecha automaticamente actual
    likes = models.IntegerField()
    public = models.BooleanField()

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    created_at = models.DateField()
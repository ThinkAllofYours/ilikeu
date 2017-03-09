from django.db import models
from django.utils import timezone
import json

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

#Create I_like_U Model_Man.
class Man(models.Model):
    phoneNumber = models.CharField(max_length=11)
    number = models.IntegerField()
    MAN = 'M'
    gender = models.CharField(max_length=1, default=MAN)
    mate_date = models.DateTimeField(blank=False, null=False)
    created_date = models.DateTimeField(default=timezone.now())
    showNumber = models.BooleanField(default=False)
    i_like_u = models.CharField(max_length=200)
    i_like_m = models.CharField(max_length=200)

    def publish(self):
        self.save()

    def __str__(self):
        return self.phoneNumber

class Woman(models.Model):
    phoneNumber = models.CharField(max_length=11)
    number = models.IntegerField()
    WOMAN = 'W'
    gender = models.CharField(max_length=1, default=WOMAN)
    mate_date = models.DateTimeField(blank=False, null=False)
    created_date = models.DateTimeField(default=timezone.now())
    showNumber = models.BooleanField(default=False)
    i_like_u = models.CharField(max_length=200)
    i_like_m = models.CharField(max_length=200)

    def publish(self):
        self.save()

    def __str__(self):
        return self.phoneNumber

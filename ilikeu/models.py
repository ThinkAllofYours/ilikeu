from django.db import models
from django.utils import timezone

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

#Create I_like_U Model.
class Man(models.Model):
    gender = 'M'
    mate_date = models.DateTimeField(blank=False, null=False)
    phoneNumber = models.CharField(max_length=11)
    number = models.IntegerField()
    password = models.CharField(max_length=20)
    choise1 = models.IntegerField()
    choise2 = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.save()

    def __str__(self):
        return self.phoneNumber

class Woman(models.Model):
    gender = 'W'
    mate_date = models.DateTimeField(blank=False, null=False)
    phoneNumber = models.CharField(max_length=11, blank=False, null=False)
    number = models.IntegerField()
    password = models.CharField(max_length=20)
    choise1 = models.IntegerField()
    choise2 = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.save()

    def __str__(self):
        return self.phoneNumber
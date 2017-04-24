from django.db import models
from django.utils import timezone

# Create your models here.
from django.utils.encoding import python_2_unicode_compatible


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

# @python_2_unicode_compatible
class Human(models.Model):
    MAN = 'M'
    WOMAN = 'W'
    GENDERS = (
        (MAN, 'MAN'),
        (WOMAN, 'WOMAN')
    )
    gender = models.CharField(max_length=1, choices=GENDERS, default=MAN)
    mate_date = models.DateField(blank=True, null=False)
    phoneNumber = models.CharField(max_length=11, blank=True, null=False)
    password = models.CharField(max_length=20)
    number = models.SmallIntegerField(null=False)
    choise1 = models.SmallIntegerField(blank=True, null=False)
    choise2 = models.SmallIntegerField(blank=True, null=False)
    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.save()

    def __str__(self):
        return self.phoneNumber
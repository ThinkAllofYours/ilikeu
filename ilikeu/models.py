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
    mate_seq = models.SmallIntegerField(blank=True, null=True)
    userName = models.CharField(max_length=30, null=True, blank=True)
    phoneNumber = models.CharField(max_length=11, blank=False, null=False)
    password = models.CharField(max_length=20)
    number = models.SmallIntegerField(null=False)
    choice1 = models.SmallIntegerField(blank=True, default=0)
    choice2 = models.SmallIntegerField(blank=True, default=0)
    created_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-mate_date', '-mate_seq', '-gender', '-number',)

    def publish(self):
        self.save()

    def __str__(self):
        return self.phoneNumber


# @python_2_unicode_compatible
class MateDates(models.Model):
    mate_date = models.DateField(blank=True, null=False)
    mate_seq = models.SmallIntegerField(blank=True, null=True)
    start_choice = models.BooleanField(default=False)
    end_choice = models.BooleanField(default=False)

    class Meta:
        ordering = ('-mate_date',)

    def publish(self):
        self.save()

    def __str__(self):
        return '%s %s %s' % (self.mate_date, self.start_choice, self.end_choice)





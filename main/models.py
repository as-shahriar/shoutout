from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=244, blank=True, null=True)
    city = models.CharField(max_length=60, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    profession = models.CharField(max_length=60, blank=True, null=True)
    blood = models.CharField(max_length=6, blank=True, null=True)
    cell = models.CharField(max_length=15, blank=True, null=True)
    img = models.ImageField(upload_to='profile_pics',
                            blank=True, default="profile_pics/default.png")

    def __str__(self):
        return self.user.username


class Comment(models.Model):
    person = models.ManyToManyField(Profile)
    comment = models.CharField(max_length=244, blank=True, null=True)
    username = models.CharField(max_length=244, blank=True, null=True)

    def __str__(self):
        return self.comment


class Post(models.Model):
    user = models.ManyToManyField(User)
    post = models.CharField(max_length=244, blank=True, null=True)
    like = models.PositiveIntegerField(default=0)
    comment = models.ManyToManyField(Comment, blank=True)
    date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.post

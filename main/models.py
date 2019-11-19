from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=244, blank=True, null=True)
    gender = models.CharField(max_length=244, blank=True, null=True)
    profession = models.CharField(max_length=244, blank=True, null=True)
    blood = models.CharField(max_length=244, blank=True, null=True)
    cell = models.CharField(max_length=244, blank=True, null=True)

    def __str__(self):
        return self.user.username


class Comment(models.Model):
    person = models.ManyToManyField(User)
    comment = models.CharField(max_length=244, blank=True, null=True)

    def __str__(self):
        return self.comment


class Post(models.Model):
    user = models.ManyToManyField(User)
    post = models.CharField(max_length=244, blank=True, null=True)
    like = models.PositiveIntegerField(default=0)
    comment = models.ManyToManyField(Comment, blank=True)

    def __str__(self):
        return self.post

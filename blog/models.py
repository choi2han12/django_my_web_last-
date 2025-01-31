from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=25, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name



class Post(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    head_image = models.ImageField(upload_to='blog/%Y/%m/%d', blank=True)
    created = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=True)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return '{}::{}'.format(self.title, self.author)

    def get_absolute_url(self):
        return '/blog/{}/'.format(self.pk)


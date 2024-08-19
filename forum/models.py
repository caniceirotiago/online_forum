from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

#TODO the author should not be null
class Forum(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Topic(models.Model):
    title = models.CharField(max_length=200)
    forum = models.ForeignKey(Forum, related_name='topics', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Post(models.Model):
    topic = models.ForeignKey(Topic, related_name='posts', on_delete=models.CASCADE)
    author =  models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:30]
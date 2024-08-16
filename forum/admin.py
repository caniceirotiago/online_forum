from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Forum, Topic, Post

admin.site.register(Forum)
admin.site.register(Topic)
admin.site.register(Post)
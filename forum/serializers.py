from rest_framework import serializers
from .models import Forum, Topic, Post


class ForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forum
        fields = '__all__'

    def validate_name(self, value):
        if not value:
            raise serializers.ValidationError("Name cannot be empty.")
        return value


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['title']

    def validate_title(self, value):
        if not value:
            raise serializers.ValidationError("Title cannot be empty.")
        return value



class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['content']

    def validate_content(self, value):
        if not value:
            raise serializers.ValidationError("Content cannot be empty.")
        return value

from .models import Forum, Topic, Post
from rest_framework import serializers
from forum.models import Topic

class ForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forum
        fields = '__all__'

    def validate_name(self, value):
        if not value:
            raise serializers.ValidationError("Name cannot be empty.")
        return value

class TopicSerializer(serializers.ModelSerializer):
    forum = serializers.PrimaryKeyRelatedField(
        queryset=Forum.objects.all(),
        required=False  # Make the forum field optional
    )

    class Meta:
        model = Topic
        fields = ['title', 'forum']

    def validate_title(self, value):
        if not value:
            raise serializers.ValidationError("Title cannot be empty.")
        return value

    def validate(self, data):
        if self.instance is None and 'forum' not in data:
            raise serializers.ValidationError({"forum": "This field is required."})
        return data

    def create(self, validated_data):
        forum = validated_data.pop('forum')  # Remove forum from the validated data
        topic = Topic.objects.create(forum=forum, created_by=self.context['request'].user, **validated_data)
        return topic

    def update(self, instance, validated_data):
        validated_data.pop('forum', None)  # Remove forum from the validated data if present
        return super().update(instance, validated_data)



class PostSerializer(serializers.ModelSerializer):
    topic = serializers.PrimaryKeyRelatedField(
        queryset=Topic.objects.all(),
        required=False  # Make the topic field optional
    )
    class Meta:
        model = Post
        fields = ['content', 'topic']

    def validate_content(self, value):
        if not value:
            raise serializers.ValidationError("Content cannot be empty.")
        return value
    def validate(self, data):
        if self.instance is None and 'topic' not in data:
            raise serializers.ValidationError({"topic": "This field is required."})
        return data
    def create(self, validated_data):
        topic = validated_data.pop('topic')
        post = Post.objects.create(topic=topic, created_by=self.context['request'].user, **validated_data)
        return post
    def update(self, instance, validated_data):
        validated_data.pop('topic', None)
        return super().update(instance, validated_data)

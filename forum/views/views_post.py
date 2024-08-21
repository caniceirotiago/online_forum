from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response

from forum.models import Post, Topic
from forum.serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet



class PostAPI(ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    def get_queryset(self):
        topic_id = self.request.query_params.get('topic_id', None)
        user_id = self.request.query_params.get('user_id', None)
        queryset = self.queryset

        if topic_id:
            queryset = queryset.filter(topic_id=topic_id)
        if user_id:
            queryset = queryset.filter(created_by_id=user_id)

        return queryset.filter(created_by=self.request.user)

    def create(self, request, *args, **kwargs):
        topic_id = self.request.query_params.get('topic_id')
        print("topic_id", topic_id)
        topic = get_object_or_404(Topic, pk=topic_id)

        data = request.data.copy()
        data['topic'] = topic.id
        data['created_by'] = request.user.id

        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




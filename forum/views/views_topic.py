from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from forum.models import Forum, Topic
from forum.serializers import TopicSerializer
from rest_framework.permissions import IsAuthenticated


class TopicAPI(ModelViewSet):
    queryset = Topic.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = TopicSerializer

    def get_queryset(self):
        forum_id = self.request.query_params.get('forum_id', None)
        user_id = self.request.query_params.get('user_id', None)
        queryset = self.queryset

        if forum_id:
            queryset = queryset.filter(forum_id=forum_id)
        if user_id:
            queryset = queryset.filter(created_by_id=user_id)

        return queryset.filter(created_by=self.request.user)

    def create(self, request, *args, **kwargs):
        forum_id = self.request.query_params.get('forum_id')
        print("forum_id", forum_id)
        forum = get_object_or_404(Forum, pk=forum_id)  # Verifica se o fórum existe

        data = request.data.copy()
        data['forum'] = forum.id  # Associa o tópico ao fórum
        data['created_by'] = request.user.id  # Associa o tópico ao usuário atual

        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




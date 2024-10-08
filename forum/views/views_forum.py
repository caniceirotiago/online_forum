from forum.models import Forum
from forum.serializers import ForumSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet


class ForumAPI(ModelViewSet):
    queryset = Forum.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ForumSerializer

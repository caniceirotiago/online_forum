
from forum.models import Post
from forum.serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet


class PostAPI(ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer




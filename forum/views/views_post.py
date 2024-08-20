from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view
from forum.models import Topic, Post
from forum.serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes



@api_view(["POST"])
@permission_classes([IsAuthenticated])
def new_post(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    request.data['topic'] = topic.id
    serializer = PostSerializer(data = request.data)
    if serializer.is_valid():
        post = serializer.save(topic=topic, author=request.user)
        post.topic = topic
        post.author = request.user
        post.save()
        return JsonResponse({'success': True, 'post_id': post.id}, status=201)
    return JsonResponse({'success': False, 'errors': serializer.errors}, status=400)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def post_list_by_topic(request, pk):
    try:
        posts = Post.objects.filter(topic = pk)
        serialize = PostSerializer(posts, many=True)
        return JsonResponse({"posts": serialize.data})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def post_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    serialize = PostSerializer(post)
    return JsonResponse(serialize.data, status=200)

@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    serializer = PostSerializer(post, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({"post": post.id})
    return JsonResponse({'errors': serializer.errors}, status=400)

@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def post_delete(request, pk):
    post = get_object_or_404(Post, pk = pk)
    post.delete()
    return JsonResponse({'message': 'Topic deleted successfully'}, status=204)




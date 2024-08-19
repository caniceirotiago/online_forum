from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view
from forum.models import Forum, Topic
from forum.serializers import TopicSerializer


@api_view(['POST'])
def new_topic(request, pk):
    forum = get_object_or_404(Forum, pk=pk)
    data = request.data.copy()
    data['forum'] = forum.id
    serializer = TopicSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({'topic': serializer.data}, status=201)
    return JsonResponse({'errors': serializer.errors}, status=400)

@api_view(['Get'])
def topic_list_by_forum(request, pk):
    try:
        topics = Topic.objects.filter(forum=pk)
        serializer = TopicSerializer(topics, many=True)
        return JsonResponse({'topics': serializer.data})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@api_view(['GET'])
def topic_detail(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    serializer = TopicSerializer(topic)
    return JsonResponse({'topic': serializer.data})

@api_view(['PUT'])
def topic_update(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    serializer = TopicSerializer(request.data, instance=topic)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({'topic': topic.id})
    return JsonResponse({'errors': serializer.errors}, status=400)

@api_view(['DELETE'])
def topic_delete(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    topic.delete()
    return JsonResponse({'message': 'Topic deleted successfully'}, status=204)



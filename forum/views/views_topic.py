from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view
from forum.models import Forum, Topic
from forum.forms import NewTopicForm

@api_view(['POST'])
def new_topic(request, pk):
    forum = get_object_or_404(Forum, pk=pk)
    form = NewTopicForm(request.data)
    if form.is_valid():
        topic = form.save(commit=False)
        topic.forum = forum
        topic.created_by = request.user
        topic.save()
        return JsonResponse({'topic': topic.id}, status=201)
    return JsonResponse({'errors': form.errors}, status=400)

@api_view(['Get'])
def topic_list_by_forum(request, pk):
    try:
        topics = Topic.objects.filter(forum=pk)
        return JsonResponse({'topics': topics})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@api_view(['GET'])
def topic_detail(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    return JsonResponse({'topic': topic})

@api_view(['PUT'])
def topic_update(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    form = NewTopicForm(request.data, instance=topic)
    if form.is_valid():
        form.save()
        return JsonResponse({'topic': topic.id})
    return JsonResponse({'errors': form.errors}, status=400)

@api_view(['DELETE'])
def topic_delete(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    topic.delete()
    return JsonResponse({'message': 'Topic deleted successfully'}, status=204)



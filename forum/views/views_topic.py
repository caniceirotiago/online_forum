from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from forum.models import Forum, Topic, Post
from forum.forms import NewTopicForm, NewPostForm
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def topic_detail(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    posts = topic.posts.all()
    posts_data = list(posts.values('id', 'message', 'created_by_id', 'created_at'))
    topic_data = {
        'id': topic.id,
        'subject': topic.subject,
        'created_by_id': topic.created_by_id,
        'created_at': topic.created_at,
        'posts': posts_data,
    }
    return JsonResponse({'topic': topic_data})

@require_http_methods(["POST"])
def new_topic(request, pk):
    forum = get_object_or_404(Forum, pk=pk)
    form = NewTopicForm(request.POST)
    if form.is_valid():
        topic = form.save(commit=False)
        topic.forum = forum
        topic.created_by = request.user  # Supondo que o usuário esteja logado
        topic.save()
        return JsonResponse({'success': True, 'topic_id': topic.id})
    return JsonResponse({'success': False, 'errors': form.errors}, status=400)
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from forum.models import Topic
from forum.forms import NewTopicForm, NewPostForm
from django.views.decorators.http import require_http_methods


@require_http_methods(["POST"])
def new_post(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    form = NewPostForm(request.POST)
    if form.is_valid():
        post = form.save(commit=False)
        post.topic = topic
        post.author = request.user  # Supondo que o usuário esteja logado
        post.save()
        return JsonResponse({'success': True, 'post_id': post.id})
    return JsonResponse({'success': False, 'errors': form.errors}, status=400)
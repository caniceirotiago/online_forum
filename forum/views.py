from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Forum, Topic, Post
from .forms import NewTopicForm
from django.shortcuts import redirect
from .forms import NewPostForm

def forum_list(request):
    forums = Forum.objects.all()
    return render(request, 'forum/forum_list.html', {'forums': forums})

def forum_detail(request, pk):
    forum = get_object_or_404(Forum, pk=pk)
    topics = forum.topics.all()
    return render(request, 'forum/forum_detail.html', {'forum': forum, 'topics': topics})

def topic_detail(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    posts = topic.posts.all()
    return render(request, 'forum/topic_detail.html', {'topic': topic, 'posts': posts})
def new_topic(request, pk):
    forum = get_object_or_404(Forum, pk=pk)
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.forum = forum
            topic.created_by = request.user  # assuming user is logged in
            topic.save()
            return redirect('forum_detail', pk=forum.pk)
    else:
        form = NewTopicForm()
    return render(request, 'forum/new_topic.html', {'form': form, 'forum': forum})
def new_post(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.author = request.user  # assuming user is logged in
            post.save()
            return redirect('topic_detail', pk=topic.pk)
    else:
        form = NewPostForm()
    return render(request, 'forum/new_post.html', {'form': form, 'topic': topic})
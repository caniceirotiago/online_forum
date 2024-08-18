from django.urls import path
from .views import views_forum, views_topic, views_post

urlpatterns = [
    # Forums
    path('forums/', views_forum.forum_list, name='forum_list'),
    path('forum/', views_forum.forum_create, name='forum_create'),
    path('forum/<int:pk>/', views_forum.forum_detail, name='forum_detail'),
    path('forum/<int:pk>/update/', views_forum.forum_update, name='forum_update'),
    path('forum/<int:pk>/delete/', views_forum.forum_delete, name='forum_delete'),

    # Topics
    path('forum/<int:pk>/new_topic/', views_topic.new_topic, name='new_topic'),
    path('topic/<int:pk>/', views_topic.topic_detail, name='topic_detail'),
    path('topics/<int:pk>/', views_topic.topic_list_by_forum, name='topic_list_by_forum'),
    path('topic/<int:pk>/update/', views_topic.topic_update, name='topic_update'),
    path('topic/<int:pk>/delete/', views_topic.topic_delete, name='topic_delete'),

    # Posts
    path('topic/<int:pk>/new_post/', views_post.new_post, name='new_post'),
]
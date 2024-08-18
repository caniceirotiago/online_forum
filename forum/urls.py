from django.urls import path
from .views import views_forum, views_topic, views_post

urlpatterns = [
    path('forums/', views_forum.forum_list, name='forum_list'),
    path('forum/', views_forum.forum_create, name='forum_create'),
    path('forum/<int:pk>/', views_forum.forum_detail, name='forum_detail'),
    path('forum/<int:pk>/update/', views_forum.forum_update, name='forum_update'),
    path('forum/<int:pk>/delete/', views_forum.forum_delete, name='forum_delete'),
    path('forum/<int:pk>/new_topic/', views_topic.new_topic, name='new_topic'),
    path('topic/<int:pk>/', views_topic.topic_detail, name='topic_detail'),
    path('topic/<int:pk>/new_post/', views_post.new_post, name='new_post'),
]
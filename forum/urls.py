from django.urls import path
from . import views

urlpatterns = [
    path('', views.forum_list, name='forum_list'),
    path('forum/<int:pk>/', views.forum_detail, name='forum_detail'),
    path('forum/<int:pk>/new_topic/', views.new_topic, name='new_topic'),
    path('topic/<int:pk>/', views.topic_detail, name='topic_detail'),
    path('topic/<int:pk>/new_post/', views.new_post, name='new_post'),
]
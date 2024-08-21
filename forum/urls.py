from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import views_forum, views_topic, views_post
from .views.views_topic import TopicAPI

api_router = DefaultRouter()
api_router.register(r'topic', TopicAPI, basename='topics')
api_router.register(r'forum', views_forum.ForumAPI, basename='forums')
api_router.register(r'post', views_post.PostAPI, basename='posts')

# GET /forums/2/topics?user_id=3
# GET /topics?forum_id=2&user_id=3
# POST /topics {forum_id: 2, ...}

urlpatterns = [
    path('', include(api_router.urls)),

]

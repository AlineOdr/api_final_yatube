from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router_version1 = DefaultRouter()
router_version1.register('posts', PostViewSet, basename='post')
router_version1.register('groups', GroupViewSet, basename='group')
router_version1.register('follow', FollowViewSet, basename='follow')
router_version1.register(r'posts\/(?P<post_id>[^/.]+)\/comments',
                         CommentViewSet, basename='comment')
urlpatterns = [
    path('v1/', include(router_version1.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]

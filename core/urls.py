from django.urls import path
from .views import GetUserVIew, PostListCreateAPIView, PostRetrieveUpdateDestroyAPIView, UserPostsListView


urlpatterns = [
path('me/', GetUserVIew.as_view(), name='get_user'),
path('posts/user/', UserPostsListView.as_view(), name='user_posts_list'),
path('posts/', PostListCreateAPIView.as_view(), name='post_list_create'),
path('posts/<str:id>/', PostRetrieveUpdateDestroyAPIView.as_view(), name='post_retrieve_update_destroy'),
]
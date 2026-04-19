from django.urls import path
from .views import CommentCreateApiView, LikeCreateApiView

urlpatterns =[
    path( 'create_comment/', CommentCreateApiView.as_view()),
    path( 'like_post/', LikeCreateApiView.as_view())


]
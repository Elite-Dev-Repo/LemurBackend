from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from .models import Post
from .serializers import PostSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

# Create your views here.

class GetUserVIew(RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
    



class UserPostsListView(ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(author=user)
    



class PostListCreateAPIView(ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)





class PostRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'



    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(author=user)
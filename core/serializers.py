from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}




class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    like_count = serializers.ReadOnlyField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'community', 'author', 'created_at', 'like_count']
        read_only_fields = ['author']



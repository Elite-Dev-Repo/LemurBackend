from rest_framework import serializers
from .models import Post
from .user_serializers import UserSerializer
from reactions.serializers import CommentSerializer






class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    like_count = serializers.ReadOnlyField()
    comment_count = serializers.ReadOnlyField()
    comments = CommentSerializer(many=True, read_only=True)
    community_name = serializers.ReadOnlyField(source='community.name')

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'community', 'author', 'created_at', 'like_count', 'comment_count','comments', 'community_name']
        read_only_fields = ['author']



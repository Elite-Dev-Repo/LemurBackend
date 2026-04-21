from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.db.models import Count

from core.models import Post
from .models import Comment, Like


# ─────────────────────────────────────────────
# COMMENTS
# ─────────────────────────────────────────────
class CommentCreateApiView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        post_id = request.data.get('post_id')
        content = request.data.get('content', '').strip()

        if not post_id:
            return Response(
                {'detail': 'post_id is required.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        if not content:
            return Response(
                {'detail': 'content is required.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        post = get_object_or_404(Post, id=post_id)

        comment = Comment.objects.create(
            user=request.user,
            post=post,
            content=content
        )

        return Response({
            'id': comment.id,
            'content': comment.content,
            'user': {
                'username': request.user.username
            },
            'created_at': comment.created_at,
        }, status=status.HTTP_201_CREATED)


# ─────────────────────────────────────────────
# LIKE / UNLIKE (TOGGLE)
# ─────────────────────────────────────────────
class LikeCreateApiView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        post_id = request.data.get('post_id')

        if not post_id:
            return Response(
                {'detail': 'post_id is required.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        post = get_object_or_404(Post, id=post_id)

        like, created = Like.objects.get_or_create(
            user=request.user,
            post=post
        )

        # ── UNLIKE ─────────────────────────────
        if not created:
            like.delete()

            # recompute safely (no broken property)
            like_count = Like.objects.filter(post=post).count()

            return Response({
                'liked': False,
                'like_count': like_count
            }, status=status.HTTP_200_OK)

        # ── LIKE ───────────────────────────────
        like_count = Like.objects.filter(post=post).count()

        return Response({
            'liked': True,
            'like_count': like_count
        }, status=status.HTTP_201_CREATED)
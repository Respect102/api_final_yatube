from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from posts.models import Group, Post
from rest_framework import filters, permissions, viewsets
from rest_framework.pagination import LimitOffsetPagination

from .mixins import CreateListViewSet
from .permissions import IsOwnerOrReadOnly
from .serializers import (CommentSerializer, FollowSerializer, GroupSerializer,
                          PostSerializer)

User = get_user_model()


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('post__id',)

    def get_queryset(self):
        post = get_object_or_404(Post.objects.all(), id=self.kwargs['post_id'])
        queryset = post.comments.all()
        return queryset

    def perform_create(self, serializer):
        post = get_object_or_404(Post.objects.all(), id=self.kwargs['post_id'])
        serializer.save(author=self.request.user, post=post)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FollowViewSet(CreateListViewSet):
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user)
        return user.follower.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

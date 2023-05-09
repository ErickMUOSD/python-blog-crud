from django_filters import OrderingFilter
from rest_framework.viewsets import ModelViewSet

from comments.api.serializer import CommentSerializer
from comments.models import Comment


class CommentApiViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    # some comments
    # some comments
    # some comments
    # some comments



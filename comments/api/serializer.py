from comments.models import Comment
from rest_framework import serializers

from posts.api.serializer import PostSerializer
from users.api.serializers import UserSerializer


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    post = PostSerializer()

    class Meta:
        model = Comment
        fields = ('content', 'created_at', 'user', 'post')

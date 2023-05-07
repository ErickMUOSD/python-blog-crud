from rest_framework import serializers

from categories.api.serializer import CategorySerializer
from posts.models import Post
from users.api.serializers import UserSerializer


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    category = CategorySerializer()

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'slug', 'miniature', 'user', 'category')

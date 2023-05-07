from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from posts.api.permissions import IsAdminOrReadOnly
from posts.api.serializer import PostSerializer
from posts.models import Post


class PostApiViewSet(ModelViewSet):
    queryset = Post.objects.filter(published=True)
    serializer_class = PostSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    permission_classes = [IsAdminOrReadOnly]
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['category']
    filterset_fields = ['category__slug']
def perform_create(self, serializer):
    serializer.save(owner=self.request.user)

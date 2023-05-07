from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from categories.api.permissions import IsAdminOrReadOnly
from categories.api.serializer import CategorySerializer
from categories.models import Category


class CategoryApiViewSet(ModelViewSet):
    queryset = Category.objects.all()
    # queryset = Category.objects.filter(published=True)
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['published','title']

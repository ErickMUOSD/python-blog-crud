from django.db import models
from django.db.models import SET_NULL, CASCADE

from posts.models import Post
from users.models import User


# Create your models here.
class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=CASCADE , null=True)
    post = models.ForeignKey(Post, on_delete=CASCADE, null=True)

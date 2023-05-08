from django.contrib import admin

from comments.models import Comment


# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'created_at', 'user', 'post')
    # list_display_links = ('id', 'content')
    # search_fields = ('content', 'user__username', 'post__title')
    # list_filter = ('created_at', 'user__username', 'post__title')
    # list_per_page = 10
    # ordering = ('-created_at',
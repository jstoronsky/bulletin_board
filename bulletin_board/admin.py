from django.contrib import admin
from bulletin_board.models import Ad, Comment
# Register your models here.


@admin.register(Ad)
class CustomAdAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'description', 'price', 'author', 'created_at', 'last_modified')


@admin.register(Comment)
class CustomCommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'ad', 'author', 'created_at')

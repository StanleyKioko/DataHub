# content/admin.py

from django.contrib import admin
from .models import Document, Comment

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploader', 'uploaded_at')
    search_fields = ('title', 'description', 'uploader__username')
    list_filter = ('uploaded_at', 'uploader')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('document', 'user', 'created_at')
    search_fields = ('text', 'user__username', 'document__title')
    list_filter = ('created_at', 'user')

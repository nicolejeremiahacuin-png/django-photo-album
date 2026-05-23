# albums/admin.py
from django.contrib import admin
from .models import Album, Photo  # This imports the models from your models.py file cleanly

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'created_at', 'is_private')
    list_filter = ('is_private', 'created_at', 'owner')
    search_fields = ('title', 'description')
    ordering = ('-created_at',)

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'album', 'title', 'uploaded_at')
    list_filter = ('uploaded_at', 'album')
    search_fields = ('title',)
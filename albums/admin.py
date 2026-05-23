from django.contrib import admin
from .models import Album, Photo

# Customizing the Album interface in the admin panel
@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'created_at', 'is_private')
    list_filter = ('is_private', 'created_at', 'owner')
    search_fields = ('title', 'description')
    ordering = ('-created_at',)

# Customizing the Photo interface in the admin panel
@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'album', 'title', 'uploaded_at')
    list_filter = ('uploaded_at', 'album')
    search_fields = ('title',)
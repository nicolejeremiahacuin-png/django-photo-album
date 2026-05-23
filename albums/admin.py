# albums/admin.py
from django.contrib import admin
from .models import Album, Photo

# 1. Customizing the Album interface in the admin panel
@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    # Ensure these fields match what is actually inside your models.py!
    list_display = ('title', 'owner', 'created_at', 'is_private')
    list_filter = ('is_private', 'created_at', 'owner')
    search_fields = ('title', 'description')
    ordering = ('-created_at',)

# 2. Customizing the Photo interface in the admin panel
@admin.register(Photo)  # <--- FIX: Register Photo here instead of Album
class PhotoAdmin(admin.ModelAdmin):  # <--- FIX: Change name to PhotoAdmin
    # Adjust these fields to match your actual Photo model fields
    list_display = ['title', 'album', 'created_at'] 
    list_filter = ['album', 'created_at']
    search_fields = ['title']
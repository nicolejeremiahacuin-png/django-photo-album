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
@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    # This is causing the crash because 'owner' and 'is_private' don't exist!
    list_display = ['title', 'owner', 'created_at', 'is_private'] 
    list_filter = ['is_private', 'created_at', 'owner']
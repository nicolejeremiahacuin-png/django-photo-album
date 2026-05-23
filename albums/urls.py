from django.urls import path
from .views import (
    AlbumListView, 
    AlbumDetailView, 
    AlbumCreateView, 
    AlbumUpdateView, 
    PhotoUploadView,
    PhotoDetailView,   # <-- ADDED THIS IMPORT
    PhotoDeleteView    # <-- ADDED THIS IMPORT
)

urlpatterns = [
    path('', AlbumListView.as_view(), name='album-list'),
    path('album/<int:pk>/', AlbumDetailView.as_view(), name='album-detail'),
    path('album/new/', AlbumCreateView.as_view(), name='album-create'),
    path('album/<int:pk>/edit/', AlbumUpdateView.as_view(), name='album-update'),
    path('album/<int:album_id>/upload/', PhotoUploadView.as_view(), name='photo-upload'),
    
    # ==============================================================================
    # 🚀 NEW PHOTO VIEW AND DELETE PATHS INSERTED HERE
    # ==============================================================================
    path('photo/<int:pk>/', PhotoDetailView.as_view(), name='photo-detail'),
    path('photo/<int:pk>/delete/', PhotoDeleteView.as_view(), name='photo-delete'),
]
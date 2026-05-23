from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Album(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # RBAC/Ownership tracking
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='albums')
    is_private = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Photo(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='photos')
    title = models.CharField(max_length=100, blank=True)
    # Cloudinary handles storage routing
    image = CloudinaryField('image')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title or 'Photo'} in {self.album.title}"
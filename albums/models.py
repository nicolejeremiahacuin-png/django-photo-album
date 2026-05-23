# albums/models.py
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Album(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    cover_image = CloudinaryField('image')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='albums')
    is_private = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Photo(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='photos')
    title = models.CharField(max_length=100, blank=True)
    image = CloudinaryField('image')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or f"Photo {self.id}"
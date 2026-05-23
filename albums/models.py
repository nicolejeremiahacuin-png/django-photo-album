from django.db import models
from django.contrib.auth.models import User
try:
    # cloudinary package may not be installed in some environments (linting/dev);
    # silence import analyzer while still attempting the real import at runtime
    from cloudinary.models import CloudinaryField  # type: ignore
except Exception:  # cloudinary not installed in this environment; fallback to ImageField
    from django.db import models as _models

    class CloudinaryField(_models.ImageField):
        """Fallback stub for CloudinaryField when cloudinary package is unavailable.
        Behaves like a normal ImageField for local development and linting.
        """
        def __init__(self, *args, **kwargs):
            # keep same signature compatibility
            super().__init__(*args, **kwargs)


class Album(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    cover_image = CloudinaryField('image') 
    
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='albums')
    created_at = models.DateTimeField(auto_now_add=True)

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
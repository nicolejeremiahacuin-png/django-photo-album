from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from .models import Album, Photo

class AlbumListView(ListView):
    model = Album
    template_name = 'albums/album_list.html'
    context_object_name = 'albums'

    def get_queryset(self):
        # Admin staff see everything; authenticated users see public albums + their own; anonymous users see only public
        if self.request.user.is_staff:
            return Album.objects.all()
        if self.request.user.is_authenticated:
            return Album.objects.filter(Q(is_private=False) | Q(owner=self.request.user))
        return Album.objects.filter(is_private=False)

class AlbumDetailView(DetailView):
    model = Album
    template_name = 'albums/album_detail.html'
    context_object_name = 'album'

class AlbumCreateView(LoginRequiredMixin, CreateView):
    model = Album
    fields = ['title', 'description', 'is_private']
    template_name = 'albums/album_form.html'
    success_url = reverse_lazy('album-list')

    def form_valid(self, form):
        # Automatically assign the logged-in user as the owner
        form.instance.owner = self.request.user
        return super().form_valid(form)

class AlbumUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Album
    fields = ['title', 'description', 'is_private']
    template_name = 'albums/album_form.html'
    success_url = reverse_lazy('album-list')

    def test_func(self):
        # RBAC Check: Only the album owner or an Admin/Staff member can modify it
        album = self.get_object()
        return self.request.user == album.owner or self.request.user.is_staff

class PhotoUploadView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Photo
    fields = ['title', 'image']
    template_name = 'albums/photo_form.html'

    def form_valid(self, form):
        # Tie the photo to the specific album from the URL route
        form.instance.album = Album.objects.get(pk=self.kwargs['album_id'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('album-detail', kwargs={'pk': self.kwargs['album_id']})

    def test_func(self):
        # RBAC Check: Only the album owner or an Admin/Staff member can add photos
        album = Album.objects.get(pk=self.kwargs['album_id'])
        return self.request.user == album.owner or self.request.user.is_staff


# ==============================================================================
# 🚀 INSERTED NEW VIEWS HERE FOR THE LIGHTBOX VIEW & DELETE ACTION
# ==============================================================================

class PhotoDetailView(DetailView):
    model = Photo
    template_name = 'albums/photo_detail.html'
    context_object_name = 'photo'

class PhotoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Photo
    template_name = 'albums/photo_confirm_delete.html'
    
    # Redirect cleanly right back to the album detail dashboard layout after deleting
    def get_success_url(self):
        return reverse_lazy('album-detail', kwargs={'pk': self.object.album.id})

    def test_func(self):
        # Strict Assignment Specification RBAC check: 
        # Only the parent album owner or an Admin/Staff member can execute the delete command
        photo = self.get_object()
        return self.request.user == photo.album.owner or self.request.user.is_staff
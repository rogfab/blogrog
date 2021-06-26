from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from .models import BlogPost


class BlogHome(ListView):
    model = BlogPost
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset
        return queryset.filter(published=True)


# ajoute la méthode login_required à la méthode d'appel du template associé
@method_decorator(login_required, name='dispatch')
class BlogCreateView(CreateView):
    model = BlogPost
    fields = ['title', 'content',]
    template_name = 'posts/blogpost_create.html'


# ajoute la méthode login_required à la méthode d'appel du template associé
@method_decorator(login_required, name='dispatch')
class BlogUpdateView(UpdateView):
    model = BlogPost
    fields = ['title', 'content', 'published',]
    template_name = 'posts/blogpost_update.html'


class BlogDetailView(DetailView):
    model = BlogPost
    context_object_name = 'post'


# ajoute la méthode login_required à la méthode d'appel du template associé
@method_decorator(login_required, name='dispatch')
class BlogDeleteView(DeleteView):
    model = BlogPost
    context_object_name = "post"
    success_url = reverse_lazy("posts:home")

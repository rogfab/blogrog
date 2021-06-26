from django.urls import path

from .views import BlogHome, BlogCreateView, BlogUpdateView, BlogDetailView, BlogDeleteView

app_name = "posts"

urlpatterns = [
    path('', BlogHome.as_view(), name="home"),
    path('create/', BlogCreateView.as_view(), name="create"),
    path('<str:slug>/', BlogDetailView.as_view(), name="post"),
    path('edit/<str:slug>/', BlogUpdateView.as_view(), name="edit"),
    path('delete/<str:slug>/', BlogDeleteView.as_view(), name="delete"),
]
from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('read-post/', views.read_post),
    path('<slug>/', views.DetailView.as_view(), name='detail'),
]
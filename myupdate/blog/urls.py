from django.conf.urls import url
from django.urls import path

from . import views
app_name = 'post'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('read-post/', views.read_post),
    url(r'^(?P<slug>[^/]*)/$', views.DetailView.as_view(), name='detail'),
]
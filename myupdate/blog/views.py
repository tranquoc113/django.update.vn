from django.http import HttpResponse
from .models import Post, Category, SubCategory
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.views.generic.base import ContextMixin
from django.views.generic import TemplateView
# Create your views here.


class IndexView(generic.ListView):
    template_name = 'pages/home.html'
    context_object_name = 'list'

    def get_queryset(self):
        return Post.objects.filter(active__in=[True]).order_by('-created_at')[0:5]


class DetailView(generic.DetailView):
    model = Post
    template_name = 'pages/detail.html'


def CategorylView(request):
    return render(request, 'pages/category.html')




def read_post(request):
    id_post = request.POST['id']
    if id_post:
        p = get_object_or_404(Post, pk=id_post)
        p.visit += 1
        p.save()

    return HttpResponse(status=201)



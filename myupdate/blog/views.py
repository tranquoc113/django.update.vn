from django.http import HttpResponse
from .models import Post, Category, SubCategory
from django.shortcuts import get_object_or_404
from django.views import generic
from django.views.generic.base import ContextMixin
from django.views.generic import TemplateView
# Create your views here.


class NavView(ContextMixin):
    def get_context_data(self, *args,**kwargs):
            context = super().get_context_data(*args, **kwargs)
            context["category"] = Category.objects.filter(active=True)
            return context


class IndexView(NavView, TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["list"] = Post.objects.filter(active=True).order_by('-created_at')[0:5]
        return context


class DetailView(generic.DetailView):
    model = Post
    template_name = 'pages/detail.html'


def read_post(request):
    id_post = request.POST['id']
    if id_post:
        p = get_object_or_404(Post, pk=id_post)
        p.visit += 1
        p.save()

    return HttpResponse(status=201)



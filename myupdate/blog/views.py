from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import Post, Menu, SubMenu
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.db.models import Q
# Create your views here.


class IndexView(generic.ListView):
    template_name = 'pages/home.html'
    context_object_name = 'list'

    def get_queryset(self):
        return Post.objects.filter(active__in=[True]).order_by('-created_at')[0:5]


def list_post(request):
    list = Post.objects.filter(active__in=[True]).order_by('-created_at')
    paginator = Paginator(list, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # print('page', page_obj.values())
    return render(request, 'pages/home.html', {'list': page_obj})


def detail_post(request, slug):
    p = Post.objects.filter(slug=slug).first()
    if p:
        p.visit += 1
        p.save()
    return render(request, 'pages/detail.html', {'post': p})


def post_category(request, slug):
    p = Post.objects.filter(Q(category__slug=slug)|Q(sub_category__slug=slug))
    return render(request, 'pages/category.html', {'post': p})


def read_post(request):
    id_post = request.POST['id']
    if id_post:
        p = get_object_or_404(Post, pk=id_post)
        p.visit += 1
        p.save()

    return HttpResponse(status=201)




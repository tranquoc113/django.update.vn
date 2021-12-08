from rest_framework.response import Response
from rest_framework import viewsets, generics, permissions, status
from rest_framework.views import APIView

from .models import Post, Category
from .serializers import CategorySerializer, PostSerializer


# Create your views here.

class CategoryViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PostViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class AuthInfor(APIView):
    def get(self, request):
        return Response({
            "x": 'oki'
        }, status=status.HTTP_200_OK)

from rest_framework.response import Response
from rest_framework import viewsets, generics, permissions, status
from rest_framework.views import APIView

from myupdate.blog.models import Post, Menu
from myupdate.blog.serializers import CategorySerializer, PostSerializer


class CategoryViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = CategorySerializer


class PostViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        return self.queryset.filter(active=True).order_by('-created_at')


class AuthInfor(APIView):
    def get(self, request):
        return Response({
            "x": 'oki'
        }, status=status.HTTP_200_OK)

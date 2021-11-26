from rest_framework.serializers import ModelSerializer
from .models import Post, Category, Tag


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

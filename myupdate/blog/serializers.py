from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from .models import Post, Menu, Tag
from ..users.models import User


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = "__all__"


class PostSerializer(ModelSerializer):
    auth = SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'summary', 'created_at', 'icon', 'auth']

    @staticmethod
    def get_auth(obj: Post):
        auth = User.objects.filter(pk=obj.author.id).first()
        print(type(auth))
        if not auth:
            return None
        return {
            'name': auth.username,
        }

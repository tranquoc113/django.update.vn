from django.contrib import admin
from .models import Category, Post, Tag
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

# Register your models here.
admin.site.register(Category)


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    form = PostForm


admin.site.register(Post, PostAdmin)

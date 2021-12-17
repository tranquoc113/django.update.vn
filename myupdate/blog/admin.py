from django.contrib import admin
from .models import Category, Post, Tag, Course, Comment, SubCategory
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

# Register your models here.
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Course)
admin.site.register(Comment)
admin.site.register(SubCategory)


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    form = PostForm


admin.site.register(Post, PostAdmin)

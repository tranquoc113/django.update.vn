from django.contrib import admin
from .models import Menu, Post, Tag, Course, Comment, SubMenu
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

# Register your models here.
admin.site.register(Menu)
admin.site.register(Tag)
admin.site.register(Course)
admin.site.register(Comment)
admin.site.register(SubMenu)


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    form = PostForm


admin.site.register(Post, PostAdmin)

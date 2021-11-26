from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField


# Create your models here.

class BaseItem(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    icon = models.ImageField(upload_to='static/image/%Y/%m/%d', null=True, blank=True)
    active = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, blank=True, max_length=200)


class Category(BaseItem):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Post(BaseItem):
    title = models.CharField(max_length=512)
    summary = models.TextField(default="")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    content = RichTextField()
    author = models.OneToOneField('users.User', on_delete=models.SET_NULL, null=True)
    visit = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return f"{self.category} - {self.title}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title + str(self.created_at) + str(self.id))
        super().save(*args, **kwargs)


class Comment(models.Model):
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="comments_post",
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    content = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    reply = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        related_name="reply_comments",
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.owner} - {self.post}"


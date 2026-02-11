#Django modules
from django.db.models import (
    CharField, 
    SlugField,
    ForeignKey,
    CASCADE,
    TextField,
    ManyToManyField,
)

#Project modules
from apps.abstracts.models import AbstractBaseModel
from apps.users.models import CustomUser


class Category(AbstractBaseModel):
    """Model representing a blog category"""
    NAME_MAX_LENGTH = 100   
    name = CharField(
        max_length=NAME_MAX_LENGTH,
        unique=True,
        verbose_name="Category Name",
    )
    slug = SlugField(
        unique=True,
        verbose_name="Category Slug",
    )
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class Tag(AbstractBaseModel):
    """Model representing a blog tag"""
    NAME_MAX_LENGTH = 50  
    name = CharField(
        max_length=NAME_MAX_LENGTH,
        unique=True,
        verbose_name="Tag Name",
    )
    slug = SlugField(
        unique=True,
        verbose_name="Tag Slug",
    )
    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

class Post(AbstractBaseModel):
    """Model representing a blog post"""
    TITLE_MAX_LENGTH = 200
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]
    author = ForeignKey(
        CustomUser,
        on_delete=CASCADE,
        related_name='posts',
        verbose_name="Author",
    )
    title = CharField(
        max_length=TITLE_MAX_LENGTH,
        verbose_name="Post Title",
    )
    slug = SlugField(
        unique=True,
        verbose_name="Post Slug",
    )
    body = TextField(
        verbose_name="Post Body",
    )
    category = ForeignKey(
        Category,
        on_delete=CASCADE,
        related_name='posts',
        verbose_name="Post Category",
    )
    tags = ManyToManyField(
        Tag,
        blank=True,
        related_name='posts',
        verbose_name="Post Tags",
    )
    status = CharField(
        choices=STATUS_CHOICES,
        default='draft',
        verbose_name="Post Status",
    )
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

class Comment(AbstractBaseModel):
    """Model representing a comment on a blog post"""
    post = ForeignKey(
        Post,
        on_delete=CASCADE,
        related_name='comments',
        verbose_name="Commented Post",
    )
    author = ForeignKey(
        CustomUser,
        on_delete=CASCADE,
        related_name='comments',
        verbose_name="Comment Author",
    )
    body = TextField(
        verbose_name="Comment Body",
    )
    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
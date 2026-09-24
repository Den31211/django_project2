from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название")
    slug = models.SlugField(max_length=100, unique=True, blank=True, verbose_name="URL")
    description = models.TextField(blank=True, verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
class Article(models.Model):
    class Status(models.TextChoices):
        DRAFT = "draft", "Черновик"
        PUBLISHED = "published", "Опубликовано"
        ARCHIVED = "archived", "В архиве"
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, unique=True, blank=True, verbose_name="URL")
    content = models.TextField(verbose_name="Содержание")
    preview = models.CharField(max_length=500, blank=True, verbose_name="Краткое описание")
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="articles",
        verbose_name="Категория"
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="articles",
        verbose_name="Автор"
    )
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.DRAFT,
        verbose_name="Статус"
    )
    views_count = models.PositiveIntegerField(default=0, verbose_name="Просмотры")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ["-created_at"]
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

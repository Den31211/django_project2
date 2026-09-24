from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, Article
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "created_at")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "author", "status", "views_count", "created_at")
    list_filter = ("status", "category", "created_at")
    search_fields = ("title", "content")
    prepopulated_fields = {"slug": ("title",)}
    list_editable = ("status",)
    date_hierarchy = "created_at"

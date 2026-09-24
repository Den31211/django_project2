from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Category, Article
class CategorySerializer(serializers.ModelSerializer):
    articles_count = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = ["id", "name", "slug", "description"]
    def get_articles_count(self,obj):
        return obj.articles.filter(status=Article.Status.PUBLISHED).count()
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name"]
class ArticleListSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    author = AuthorSerializer(read_only=True)
    class Meta:
        model = Article
        fields = [
            "id", "title", "slug", "preview",
            "category", "author", "status",
            "views_count", "created_at"
        ]
class ArticleDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    author = AuthorSerializer(read_only=True)
    class Meta:
        model = Article
        fields = [
            "id", "title", "slug", "content", "preview",
            "category", "author", "status",
            "views_count", "created_at", "updated_at",
        ]

from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from .models import Category, Article
from .serializers import (
    CategorySerializer,
    ArticleListSerializer,
    ArticleDetailSerializer
)
class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
class ArticleListAPIView(generics.ListAPIView):
    serializer_class = ArticleListSerializer
    def get_queryset(self):
        queryset = Article.objects.filter(status=Article.Status.PUBLISHED)
        # Фильтрация по категории (?category=slug)
        category_slug = self.request.query_params.get("category")
        search = self.request.query_params.get("search")
        if search:
            queryset = queryset.filter(title__icontains=search)
        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)
        return queryset
    
class ArticleDetailAPIView(generics.RetrieveAPIView):
    queryset = Article.objects.filter(status=Article.Status.PUBLISHED)
    serializer_class = ArticleDetailSerializer
    lookup_field = "slug"
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        # Увеличиваем счётчик просмотров
        instance.views_count += 1
        instance.save(update_fields=["views_count"])
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

from django.urls import path
from .views import (
    CategoryListAPIView,
    ArticleListAPIView,
    ArticleDetailAPIView
)
urlpatterns = [
    path("categories/", CategoryListAPIView.as_view()),
    path("articles/", ArticleListAPIView.as_view()),
    path("articles/<slug:slug>/", ArticleDetailAPIView.as_view()),
]

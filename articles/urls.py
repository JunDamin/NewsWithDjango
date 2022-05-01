from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    path("<int:pk>", views.ArticleDetail.as_view(), name="detail"),
    path("search", views.SearchView.as_view(), name="search",),
]
from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    path("<int:pk>", views.ArticleDetail.as_view(), name="detail"),
    path("search", views.SearchView.as_view(), name="search",),
    path("upload", views.UploadView.as_view(), name="upload",),
    # path("update", views.UpdateView.as_view(), name="update",),
]
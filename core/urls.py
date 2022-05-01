from django.urls import path
from articles import views as article_views

app_name = "core"

urlpatterns = [path("", article_views.HomeView.as_view(), name="home"),]
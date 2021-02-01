from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name="blog_home"),
    path('<slug:slug>/', views.DetailView.as_view(), name='post_detail'),
]
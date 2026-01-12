from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog_home'),
    path('<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('add/', views.add_blog, name='add_blog'),
    path('update/<int:blog_id>/', views.update_blog, name='update_blog'),
    path('delete/<int:blog_id>/', views.delete_blog, name='delete_blog'),
]
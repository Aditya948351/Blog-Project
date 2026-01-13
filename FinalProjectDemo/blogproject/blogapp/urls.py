from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('add', views.add_blog, name='add-blog'),
    path('update/<int:blog_id>/', views.update_blog, name='update-blog'),
    path('delete/<int:blog_id>/', views.delete_blog, name='delete-blog'),
    
]

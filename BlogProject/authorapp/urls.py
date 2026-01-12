from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='author_home'),
    path('add', views.add_author, name='add_author'),
    path('update/<int:author_id>/', views.update_author, name='update_author'),
    path('delete/<int:author_id>/', views.delete_author, name='delete_author'),
    
]
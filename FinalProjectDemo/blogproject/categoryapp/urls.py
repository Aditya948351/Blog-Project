from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='category-home'),
    path('add', views.add_category, name='add-category'),
    path('update/<int:category_id>/', views.update_category, name='update-category'),
    path('delete/<int:category_id>/', views.delete_category, name='delete-category'),
    
]

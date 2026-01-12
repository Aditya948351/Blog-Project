from django.shortcuts import render, redirect, get_object_or_404
from .models import Category
from .forms import CategoryForm

# Create your views here.

def home(request):
    categories = Category.objects.all()
    return render(request, 'categoryapp/category_list.html', {'categories': categories})

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_home')
    else:
        form = CategoryForm()
    return render(request, 'categoryapp/add_category.html', {'form': form})

def update_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_home')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'categoryapp/update_category.html', {'form': form})

def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        category.delete()
        return redirect('category_home')
    return render(request, 'categoryapp/category_confirm_delete.html', {'category': category})

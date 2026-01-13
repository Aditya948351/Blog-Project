from django.shortcuts import redirect, render
from .forms import CategoryForm
from .models import Category

# Create your views here.

def home(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        return render(request, 'categoryapp/categorylist.html',{'categories': categories})
    
    
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category-home')
    else:
        form = CategoryForm()
    return render(request, 'categoryapp/addcategory.html', {'form': form})
    

def update_category(request, category_id):
    category = Category.objects.get(id=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category-home')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'categoryapp/addcategory.html', {'form': form})



def delete_category(request, category_id):
    category = Category.objects.get(id=category_id)
    category.delete()
    return redirect('category-home')
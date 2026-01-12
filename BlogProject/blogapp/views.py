from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from .forms import BlogForm

# Create your views here.

def home(request):
    blogs = Blog.objects.all()
    return render(request, 'blogapp/blog_list.html', {'blogs': blogs})

def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, 'blogapp/blog_detail.html', {'blog': blog})

def add_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_home')
    else:
        form = BlogForm()
    return render(request, 'blogapp/add_blog.html', {'form': form})

def update_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog_home')
    else:
        form = BlogForm(instance=blog)
    return render(request, 'blogapp/update_blog.html', {'form': form})

def delete_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method == 'POST':
        blog.delete()
        return redirect('blog_home')
    return render(request, 'blogapp/blog_confirm_delete.html', {'blog': blog})
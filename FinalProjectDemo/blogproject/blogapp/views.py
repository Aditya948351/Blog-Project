from django.shortcuts import redirect, render
from .forms import  BlogForm
from .models import Blog

# Create your views here.

def home(request):
    if request.method == 'GET':
        blogs = Blog.objects.all()
        return render(request, 'blogapp/bloglist.html',{'blogs': blogs})
    
    
def add_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog-home')
    else:
        form = BlogForm()
    return render(request, 'blogapp/addblog.html', {'form': form})
    

def update_blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog-home')
    else:
        form = BlogForm(instance=blog)
    return render(request, 'blogapp/updateblog.html', {'form': form})



def delete_blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    blog.delete()
    return redirect('blog-home')
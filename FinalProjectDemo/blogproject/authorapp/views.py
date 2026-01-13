from django.shortcuts import redirect, render
from .forms import AuthorForm
from .models import Author
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(  )
def home(request):
    if request.method == 'GET':
        authors = Author.objects.all()
        return render(request, 'authorapp/authorlist.html',{'authors': authors})
    
@login_required(  )    
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author-home')
    else:
        form = AuthorForm()
    return render(request, 'authorapp/addauthor.html', {'form': form})
    
@login_required()
def update_author(request, author_id):
    author = Author.objects.get(id=author_id)
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('author-home')
    else:
        form = AuthorForm(instance=author)
    return render(request, 'authorapp/addauthor.html', {'form': form})


@login_required( )
def delete_author(request, author_id):
    author = Author.objects.get(id=author_id)
    author.delete()
    return redirect('author-home')
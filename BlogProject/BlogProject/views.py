from django.shortcuts import render
from .forms import UserRegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm

def homepage(request):
    
    # Logic for rendering the homepage
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            form = AuthenticationForm()
            return render(request, 'login.html', {'form': form, 'error': 'Invalid credentials'})    
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form, 'error': 'Invalid credentials'})
    

def logout_view(request):
    logout(request)
    return redirect('login')
    

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
            # Redirect to a success page.
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})
from django.shortcuts import redirect, render
from .forms import ProfileForm
# Create your views here.

def update_profile(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            user = request.user
            form = ProfileForm(request.POST, request.FILES,instance=user)
            if form.is_valid():
                form.save()
                return redirect('homepage')
            else:
                return render(request, 'profileapp/updateprofile.html', {'form': form})
        else:
            return redirect('login')
    else:
        form = ProfileForm()
    return render(request, 'profileapp/updateprofile.html', {'form': form})
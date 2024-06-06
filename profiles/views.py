from django.shortcuts import render, redirect
from .forms import ProfileForm
from django.contrib import messages

def profile__view(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Siz qeydiyyatdan keçdiniz!")
            return redirect('profile')
        else:
            messages.error(request, "Form validation failed. Please check your inputs.")
    else:
        form = ProfileForm()
    
    return render(request, "base.html", {'form': form})

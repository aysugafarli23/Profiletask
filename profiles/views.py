import os
import pdfkit
from django.template.loader import render_to_string
from weasyprint import HTML
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProfileForm
from django.contrib import messages
from.models import Profile



def profile__view(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, "Siz qeydiyyatdan keçdiniz!")
            return redirect('profile')
        else:
            messages.error(request, "Form validation failed. Please check your inputs.")
    else:
        form = ProfileForm()
    
    return render(request, "base.html", {'form': form})

# def profile_list_view(request,id):
#     # os.add_dll_directory(r"C:\Program F/iles\gtk-3.8.1\bin")
#     profile = Profile.objects.get(id=id)
#     html = render_to_string('cv_template.html', {'profile': profile})
#     pdf = pdfkit.from_string(html, False , configuration=settings.PDFKIT_CONFIG, options = settings.PDFKIT_OPTIONS)
    
#     response = HttpResponse(pdf,content_type = 'application/pdf')
#     response['Content-Disposition'] = f'attachment; filename = "{profile.name}_{profile.lastname}_profile.pdf"'
    
#     return response

def profile_list_view(request, id):
    profile = get_object_or_404(Profile, id=id)
    
    html_string = render_to_string('cv_template.html', {'profile': profile})
    config = pdfkit.configuration(wkhtmltopdf=settings.PDFKIT_CONFIG['wkhtmltopdf'])
    pdf = pdfkit.from_string(html_string, False, configuration=config, options=settings.PDFKIT_OPTIONS)
    
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{profile.username}_{profile.lastname}_profile.pdf"'

    return response

def list__view(request):
    profiles = Profile.objects.all()
    context={
        "profiles":profiles
    }
    return render(request, "list.html", context)
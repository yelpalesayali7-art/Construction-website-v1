from django.shortcuts import render,redirect
# from django.shortcuts import Http 
from .models import Service,Project
from .forms import ContactForm
from django.contrib import messages

# Create your views here.
from django.http import HttpResponse,FileResponse


import os
from django.http import FileResponse
from django.conf import settings

def mohit(request):
    # Path to your image file (adjust directory as needed)
    img_path = os.path.join(settings.BASE_DIR, 'templates', 'static', 'image.png')
    
    # Open the file in binary read mode ('rb')
    img = open(img_path, 'rb')
    
    # Return it directly as a response
    return FileResponse(img, content_type='image/png')

#---------------------------------------------------------------------
def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def services(request):
    services = Service.objects.all()

    return render(request, "services.html", {
        "services": services
    })

def website (request):
    return HttpResponse("Hello Django")

def projects(request):
    projects = Project.objects.all()

    return render(request, "projects.html", {
        "projects": projects
    })

def contact(request):

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, "Thank you! Your message has been sent successfully.")
        return redirect("/contact/")
        
    else:
        form = ContactForm()

    return render(request, "contact.html", {
        "form": form
    })

def blog(request):
    return render(request,"blog.html")



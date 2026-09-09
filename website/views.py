from django.shortcuts import render
# from django.shortcuts import Http 



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
    return render(request, "services.html")

def website (request):
    return HttpResponse("Hello Django")

def projects(request):
    return render(request, "projects.html")

def contact(request):
    return render(request,"contact.html")

def blog(request):
    return render(request,"blog.html")



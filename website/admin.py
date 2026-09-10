from django.contrib import admin
from .models import Service, Project, ContactMessage

admin.site.register(Service)
admin.site.register(Project)
admin.site.register(ContactMessage)
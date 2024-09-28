from django.contrib import admin #type: ignore
from .models import Property

# Register your models here.
admin.site.register(Property)

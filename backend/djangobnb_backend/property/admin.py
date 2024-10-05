from django.contrib import admin #type: ignore
from .models import Property, Reservation

# Register your models here.
admin.site.register(Property)
admin.site.register(Reservation)

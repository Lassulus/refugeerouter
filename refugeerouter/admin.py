from django.contrib import admin
from .models import Group, Refugee, Flat, Driver, Trip, Notifier

# Register your models here.
admin.site.register(Group)
admin.site.register(Refugee)
admin.site.register(Flat)
admin.site.register(Driver)
admin.site.register(Trip)
admin.site.register(Notifier)
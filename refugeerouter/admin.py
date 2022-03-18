from django.contrib import admin
from .models import Group, Accomodation, Driver, Notifier

# Register your models here.
admin.site.register(Group)
admin.site.register(Accomodation)
admin.site.register(Driver)
admin.site.register(Notifier)

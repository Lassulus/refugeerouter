from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Booking, Group, Refugee, Flat, User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserAdmin(BaseUserAdmin):
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('username', 'first_name', 'last_name', 'contact_data', 'is_superuser', 'is_staff', 'is_notifier', 'is_authority_supporters', 'is_flat_owner', 'is_dispatcher', 'is_paramedic', 'is_driver',)
    list_filter = ('is_superuser', 'is_staff', 'is_notifier', 'is_authority_supporters', 'is_flat_owner', 'is_dispatcher', 'is_paramedic' )
    fieldsets = (
        (None, {'fields': ('first_name', 'last_name', 'password',)}),
        ('Contact Data', {'fields': ('contact_data',)}),
        ('Flags', {'fields': ('is_superuser', 'is_staff', 'is_notifier', 'is_authority_supporters', 'is_flat_owner', 'is_dispatcher',)}),
        ('seats', {'fields': ('num_seats',)}),
    )


# Register your models here.
admin.site.register(Booking)
admin.site.register(Group)
admin.site.register(Refugee)
admin.site.register(Flat)
admin.site.register(User, UserAdmin)




from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.

class MyUserAdmin(BaseUserAdmin):
    list_display = ('first_name','middle_name', 'last_name', 'email',  'is_active', 'is_staff', 'is_admin')
    search_fields = ('first_name', 'email')
    filter_horizontal = ()
    list_filter = ('last_login',)
    fieldsets = ()

    add_fieldsets = (
        (None, {
            'classes': ('wide'),
            'fields': ('first_name' , 'middle_name' , 'last_name' , 'phone_number', 'roll_number', 'application_number', 'uid', 'section', 'dob', 'course', 'admitted_through', 'applied_year', 'address', 'city', 'state', 'country','email', 'password1', 'password2'),
        }),
    )
    ordering = ('first_name', 'middle_name', 'last_name', 'email',)

admin.site.register(Student, MyUserAdmin)
admin.site.register(Stu_Register)
admin.site.register(Event)
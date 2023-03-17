from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Permission
from sbte.forms import  UserChangeForm, UserRegisterationForm
from sbte.models import *


class CustomUserAdmin(UserAdmin):
    add_form = UserRegisterationForm
    form = UserChangeForm
    model = User
    list_display = ('username','user_type','email', 'is_staff', 'is_active','is_admin')
    list_filter = ('email', 'is_staff', 'is_active','is_superuser','is_admin')
    
    fieldsets = (
        (None, {'fields': ('email', 'is_staff', 'is_superuser','gender','dob','mobile',
                          'password','is_admin', 'first_name','last_name','is_active',)}),
        ('Groups', {'fields': ('groups',)}),
        ('Permissions', {'fields': ('user_permissions',)}),
    )
    add_fieldsets = (
        (None, {'fields': ('email', 'is_staff', 'is_superuser','is_admin','gender', 'password1', 'password2')}),
        ('Groups', {'fields': ('groups',)}),
        ('Permissions', {'fields': ('user_permissions',)}),
    )
    
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, CustomUserAdmin)
admin.site.register(Institute)
admin.site.register(Program)
admin.site.register(AcademicSession)
admin.site.register(Permission)
admin.site.register(Student)
admin.site.register(Exams)
admin.site.register(CourseLe)


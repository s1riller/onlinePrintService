from django.contrib import admin
from .models import CustomUser, File, UserProfile


# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username','first_name','last_name','phone_number']
admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(File)
admin.site.register(UserProfile)
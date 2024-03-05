from django.contrib import admin
from .models import Address, PhoneNumber, Profile

admin.site.register(PhoneNumber)
admin.site.register(Address)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)  # Исправлено: теперь это кортеж

# Не забудьте также зарегистрировать Profile с его админ-классом
admin.site.register(Profile, ProfileAdmin)
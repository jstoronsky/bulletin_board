from django.contrib import admin
from users.models import User
# Register your models here.


@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'email', 'role', 'phone', 'last_login')

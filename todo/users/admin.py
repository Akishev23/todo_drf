from django.contrib import admin
from .models import Users

# Register your models here.


@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    model = Users
    list_display = ('id', 'username', 'first_name', 'last_name', 'photo', 'age',
                    'email','is_staff', 'is_active', 'date_joined', 'last_login')

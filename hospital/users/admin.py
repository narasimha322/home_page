from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone', 'get_user_type', 'is_active', 'date_joined')  # Ensure date_joined exists
    list_filter = ('is_staff', 'is_active', 'date_joined')  # Ensure date_joined exists
    search_fields = ('username', 'email', 'phone')

    def get_user_type(self, obj):
        return "Staff" if obj.is_staff else "Normal User"
    get_user_type.short_description = 'User Type'


admin.site.register(User, UserAdmin)

from django.contrib import admin
from apps.users.models import CustomUser


@admin.register(CustomUser)
class ProductAdmin(admin.ModelAdmin):
    fields = ['username', 'password', 'admin', 'is_active', 'is_staff', 'last_login', 'date_joined']
    list_display = ('username',)
    list_display_links = list_display
    readonly_fields = ['date_joined', 'last_login']
    search_fields = ('username',)

    def save_model(self, request, obj, form, change):
        if obj.password != form.initial.get('password'):
            obj.set_password(obj.password)
        obj.save()

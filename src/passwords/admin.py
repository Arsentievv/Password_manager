from django.contrib import admin
from passwords.models import Service


class ServiceAndPasswordAdmin(admin.ModelAdmin):
    list_display = ['id', 'service_name', 'hashed_password']
    prepopulated_fields = {'slug': ('service_name', )}


admin.site.register(Service, ServiceAndPasswordAdmin)


from django.contrib import admin

from auth_system_app.models import AccessCode

# Register your models here.
@admin.register(AccessCode)
class AccessCodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'is_used', 'issued_to', 'created_at')
    list_filter = ('is_used',)
    search_fields = ('code',)
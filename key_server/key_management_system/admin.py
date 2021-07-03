from django.contrib import admin  # noqa F401

from key_server.key_management_system.models import Key

# Register your models here.


@admin.register(Key)
class KeyAdmin(admin.ModelAdmin):
    pass

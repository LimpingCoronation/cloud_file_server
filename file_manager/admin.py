from django.contrib import admin

from .models import File


class FileAdmin(admin.ModelAdmin):
    fields = ['user', 'file']


admin.site.register(File, FileAdmin)

from django.contrib import admin
from .models import Client, Meet, Note

@admin.register(Note)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name',)
    ordering = ('created_at',)


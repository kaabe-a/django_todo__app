from django.contrib import admin
from . models import Todo

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title','description','created','slug')
    # list_editable = ('created',)
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('created',)
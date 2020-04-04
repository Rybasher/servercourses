from django.contrib import admin
from .models import *
# Register your models here.


class ChildsAdmin(admin.ModelAdmin):
    list_display = ('name', 'paid', 'homework')
    list_display_links = ('name',)


admin.site.register(Child, ChildsAdmin)
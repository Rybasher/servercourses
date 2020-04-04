from django.contrib import admin
from .models import *
# Register your models here.


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'telegram', 'email')
    list_display_links = ('name',)


admin.site.register(Teacher, TeacherAdmin)


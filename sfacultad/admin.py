from django.contrib import admin
"""
Usuario admin: alfonso
password: gz0cf5JGA
"""
# Register your models here.
from .models import comments

class Comments_Admin(admin.ModelAdmin):
    list_display = ('matricula', 'aula', 'num', 'ip_disp')
    pass

admin.site.register(comments, Comments_Admin)

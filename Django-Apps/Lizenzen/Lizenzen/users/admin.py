from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import admin_verwalter, kunde

admin.site.register(admin_verwalter)
admin.site.register(kunde)

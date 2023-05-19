from django.contrib import admin
from .models import AdminVerwalter, Kunde

# Register your models here.
admin.site.register(AdminVerwalter)
admin.site.register(Kunde)
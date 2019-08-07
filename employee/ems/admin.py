from django.contrib import admin

# Register your models here.

from .models import Employee,sample

admin.site.register(Employee)

admin.site.register(sample)

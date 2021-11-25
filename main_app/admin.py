from django.contrib import admin
# import your models here
from .models import Month, Expenses

# Register your models here
admin.site.register(Month)

admin.site.register(Expenses)
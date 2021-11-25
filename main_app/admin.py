from django.contrib import admin
# import your models here
from .models import Month, Expense

# Register your models here
admin.site.register(Month)

admin.site.register(Expense)
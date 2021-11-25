from django.forms import ModelForm
from .models import Expense

class ExpenseForm(ModelForm):
  class Meta:
    model = Expense
    fields = ['date', 'price', 'reason', 'worthit', 'recurring', 'paid']
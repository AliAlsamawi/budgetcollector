from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView
from .models import Month
from .forms import ExpenseForm



# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

class Months:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, budget, year):
    self.name = name
    self.budget = budget
    self.year = year



def months_index(request):
  months = Month.objects.all()
  return render(request, 'months/index.html', { 'months': months })


def months_detail(request, month_id):
  month = Month.objects.get(id=month_id)
  expense_form = ExpenseForm()
  return render(request, 'months/detail.html', {
    'month': month, 'Expense_form': expense_form
  })


class MonthCreate(CreateView):
  model = Month
  fields = '__all__'
  success_url = '/months/'

class MonthDelete(DeleteView):
  model = Month
  success_url = '/months/'

  def add_expense(request, month_id):
    form = ExpenseForm(request.POST)
    if form.is_valid():
      new_expense = form.save(commit=False)
      new_expense.month_id = month_id
      new_expense.save()
    return redirect("months_detail", month_id=month_id)

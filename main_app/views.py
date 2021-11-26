from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Month
from .forms import ExpenseForm
from django.contrib.auth.views import LoginView



# Define the home view
class Home(LoginView):
  template_name = 'home.html'

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
    'month': month, 'expense_form': expense_form
  
  })


class MonthCreate(CreateView):
  model = Month
  fields = '__all__'
  success_url = '/months/'
  def form_valid(self, form):
    form.instance.user = self.request.user  
    return super().form_valid(form)

class MonthDelete(DeleteView):
  model = Month
  success_url = '/months/'
def add_expense(request, month_id):
  form = ExpenseForm(request.POST)
  if form.is_valid():
    new_expense = form.save(commit=False)
    new_expense.month_id = month_id
    new_expense.save()
  return redirect('months_detail', month_id=month_id)


def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('months_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)

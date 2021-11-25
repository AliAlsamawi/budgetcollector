from django.shortcuts import render
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
  # instantiate FeedingForm to be rendered in the template
  expense_form = ExpenseForm()
  return render(request, 'months/detail.html', {
    # include the cat and feeding_form in the context
    'month': month, 'expense_form': expense_form
  })

class MonthCreate(CreateView):
  model = Month
  fields = '__all__'
  success_url = '/months/'

class MonthDelete(DeleteView):
  model = Month
  success_url = '/months/'
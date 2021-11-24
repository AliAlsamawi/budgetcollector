from django.shortcuts import render
from .models import Month



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
  return render(request, 'months/detail.html', { 'month': month })
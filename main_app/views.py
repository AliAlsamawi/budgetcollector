from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')

def about(request):
  return render(request, 'about.html')

class Months:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, budget, year):
    self.name = name
    self.budget = budget
    self.year = year


months = [
  Months('March', 1000, 2021),
  Months('apirl', 1000, 2021),
  Months('Feb', 1000, 2021),
  Months('Dec', 1000, 2021),
]
def months_index(request):
  return render(request, 'months/index.html', { 'months': months })

def home(request):
  return render(request, 'home.html')
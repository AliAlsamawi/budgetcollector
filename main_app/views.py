from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')

def about(request):
  return render(request, 'about.html')

class months:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, budget):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age
months = [
  months('Lolo', 'tabby', 'Kinda rude.', 3),
  months('Sachi', 'tortoiseshell', 'Looks like a turtle.', 0),
  months('Fancy', 'bombay', 'Happy fluff ball.', 4),
  months('Bonk', 'selkirk rex', 'Meows loudly.', 6)
]
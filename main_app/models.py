from django.db import models
from django.urls import reverse

MEALS = (
  ('B', 'Breakfast'),
  ('L', 'Lunch'),
  ('D', 'Dinner')
)

class Month(models.Model):
  name = models.CharField(max_length=100)
  year = models.CharField(max_length=100)
  budget = models.IntegerField()
class Expenses(models.Model):
  date = models.DateField()
  price = models.IntegerField()
  reason = models.CharField(max_length=100)
  worthit = models.CharField(max_length=1)
  recurring = models.CharField(max_length=1)
  paid = models.CharField(max_length=1)

  def __str__(self):
    return self.name
  def get_absolute_url(self):
    return reverse('months_detail', kwargs={'month_id': self.id})

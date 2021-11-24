from django.db import models
from django.urls import reverse

class Month(models.Model):
  name = models.CharField(max_length=100)
  year = models.CharField(max_length=100)
  budget = models.IntegerField()

  def __str__(self):
    return self.name
  def get_absolute_url(self):
    return reverse('months_detail', kwargs={'month_id': self.id})

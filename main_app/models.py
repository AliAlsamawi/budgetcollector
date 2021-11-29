from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

WORTHIT = (
  ('Y', 'Yes'),
  ('N', 'No'),
)
RECURRING = {
  ('Y', 'Yes'),
  ('N', 'No'), 
}
PAID = {
  ('Y', 'Yes'),
  ('N', 'No'), 
}

class Month(models.Model):
  name = models.CharField(max_length=100)
  year = models.CharField(max_length=100)
  budget = models.IntegerField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('months_detail', kwargs={'month_id': self.id})

class Expense(models.Model):
  date = models.DateField()
  price = models.IntegerField()
  reason = models.TextField(max_length=300)
  worthit = models.CharField(
    max_length=1,
    choices=WORTHIT,
    )
  recurring = models.CharField(
    max_length=1,
    choices=RECURRING,
    )
  paid = models.CharField(
    max_length=1,
    choices=PAID,
    # default=PAID[0][0]
    )

  month = models.ForeignKey(Month, on_delete=models.CASCADE)
  def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
    return f"{self.get_worthit_display()} on {self.date}"

  def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
    return f"{self.get_recurring_display()} on {self.date}"

  def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
    return f"{self.get_paid_display()} on {self.date}"
class Meta:
    ordering = ['-date']
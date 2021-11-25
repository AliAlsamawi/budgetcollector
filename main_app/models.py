from django.db import models
from django.urls import reverse

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

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('months_detail', kwargs={'month_id': self.id})

class Expenses(models.Model):
  date = models.DateField('Expenses date')
  price = models.IntegerField()
  reason = models.CharField(max_length=100)
  worthit = models.CharField(
    max_length=1,
    choices=WORTHIT,
    # default=WORTHIT[0][0]
    )
  recurring = models.CharField(
    max_length=1,
    choices=RECURRING,
    # default=RECURRING[0][0]
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
from django.db import models

# Create your models here.
class WeeklyTimesheet(models.Model):
    week_ending = models.DateField()
    day = models.CharField(max_length=20)
    start_time = models.TimeField()
    end_time = models.TimeField()

class Nanny(models.Model):
    name = models.CharField(max_length=30)
    rate = models.DecimalField(max_digits=4, decimal_places=2)
    
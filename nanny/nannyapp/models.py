from django.db import models
from datetime import date

# Create your models here.
class Week(models.Model):
    week_ending = models.DateField(name="Week Ending")

    def __unicode__(self):
        return str(self.week_ending)

class Day(models.Model):
    day = models.CharField(max_length=20, name="Day")
    
    def __unicode__(self):
        return str(self.day)
    
class DailyTimesheet(models.Model):
    week_ending = models.ForeignKey(Week)
    day = models.ForeignKey(Day)
    start_time = models.TimeField()
    end_time = models.TimeField()
    
    def __unicode__(self):
        return str(self.week_ending ) + ", " + str(self.day)

class Nanny(models.Model):
    name = models.CharField(max_length=30)
    rate = models.DecimalField(max_digits=4, decimal_places=2)
    
    def __unicode__(self):
        return self.name


    
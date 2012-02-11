from nannyapp.models import Week
from nannyapp.models import Day
from nannyapp.models import DailyTimesheet
from nannyapp.models import Nanny
from django.contrib import admin



#class DailyTimesheetAdmin(admin.ModelAdmin):
#    list_display = ('week_ending', 'day', 'start_time', 'end_time')

admin.site.register(Week)
admin.site.register(Day)
admin.site.register(DailyTimesheet)
admin.site.register(Nanny)
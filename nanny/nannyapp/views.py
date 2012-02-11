# Create your views here.
from django.http import HttpResponse
from nannyapp.models import DailyTimesheet
from nannyapp.models import Week
from django.template import Context, loader

def index(request):
    """docstring for index(request):"""
    all_weeks_list = Week.objects.all()
    t = loader.get_template('weeks/index.html')
    c = Context ({
        'all_weeks_list' : all_weeks_list,
    })
    return HttpResponse(t.render(c))

def detail(request, week_id):
    return HttpResponse("you are looking at id %s." % week_id)
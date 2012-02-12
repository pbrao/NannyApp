# Create your views here.
from django.http import HttpResponse
from nannyapp.models import DailyTimesheet
from nannyapp.models import Week
from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404

def index(request):
    """docstring for index(request):"""
    all_weeks_list = Week.objects.all()
    print all_weeks_list
    return render_to_response('weeks/index.html', {'all_weeks_list' : all_weeks_list})

def detail(request, week_id):
    #w = get_object_or_404(DailyTimesheet, week_ending = week_id)
    w = DailyTimesheet.objects.filter(week_ending = week_id)
    print w
    return render_to_response('weeks/detail.html', {'week' : w }, context_instance = RequestContext(request))
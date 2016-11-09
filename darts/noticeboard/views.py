from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, timedelta

from noticeboard.models import notice

# Create your views here.

def noticeboard(request):
    last_month = datetime.utcnow() - timedelta(months=1)
    posts = notice.objects.filter(created_at__gt=last_month)
    tempate = 

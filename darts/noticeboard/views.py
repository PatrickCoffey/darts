from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, timedelta
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from noticeboard.models import Notice
from noticeboard.forms import NoticeForm

# Create your views here.

def noticeboard(request):
    last_month = datetime.utcnow() - timedelta(30)
    notices = Notice.objects.all()
    context = {"notices": notices}
    return render(request, "noticeboard.html", context)

def individual_notice(request, slug):
    notice = get_object_or_404(Notice, slug=slug)
    context = {"notice": notice}
    return render(request, "notice.html", context)

@login_required(login_url='/accounts/login/')
def add_notice(request):
    form = NoticeForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    context = {"form": form}
    return render(request, "addnotice.html", context)
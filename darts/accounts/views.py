from django.shortcuts import render, HttpResponseRedirect, RequestContext, render_to_response
from django.contrib import auth
#from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from accounts.forms import LoginForm

# Create your views here.

def login(request):
    form = LoginForm(request.POST or None)
    context = {"form": form}
    if form.is_valid():
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user == None:
            msg = "Error with username or password. Please try again!"
            messages.add_message(request, messages.ERROR, msg)
        else:
            auth.login(request, user)
            return HttpResponseRedirect("/")
    return render(request, "login.html", context)


@login_required(login_url='/accounts/login/')
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


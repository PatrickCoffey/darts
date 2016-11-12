"""darts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from scoreboard.views import test, new_event, view_games, view_teams, current_event
from noticeboard.views import noticeboard, individual_notice, add_notice
from accounts.views import login, logout

urlpatterns = [
    # admin urls
    url(r'^admin/', admin.site.urls),
    
    # index
    url(r'^$', test, name='test'),
    
    # noticeboard
    url(r'^noticeboard/addnotice', add_notice, name='addnotice'),
    url(r'^noticeboard/(?P<slug>[^\.]+)', individual_notice), 
    url(r'^noticeboard/', noticeboard, name='noticeboard'),
    
    # scoreboard
    url(r'^scoreboard/newevent', new_event, name='newevent'),
    url(r'^scoreboard/viewgames', view_games, name='viewgames'),
    url(r'^scoreboard/viewteams', view_teams, name='viewteams'),
    url(r'^events/(?P<pk>[^\.]+)', current_event),
    
    # accounts
    url(r'^accounts/logout', logout, name='logout'),
    url(r'^accounts/login', login, name='login')
]

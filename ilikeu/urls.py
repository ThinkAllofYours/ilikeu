from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^vote/(?P<mate_date>\d+)/(?P<number>\d+)/$', views.vote, name='vote'),
    url(r'^vote/result/(?P<mate_date>\d+)/(?P<number>\d+/)$', views.result, name='vote_result'),
    url(r'^login/$', views.login, name='login'),
]


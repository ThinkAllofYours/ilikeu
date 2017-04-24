from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # url(r'^$', auth_views.login, name='login', kwargs={'template_name': 'blog/login.html'}),
    url(r'^$', views.home, name='home'),
    url(r'^vote/(?P<mate_date>\d+)/(?P<number>\d+)/$', views.vote, name='vote'),
    url(r'^vote/result/(?P<mate_date>\d+)/(?P<number>\d+/)$', views.result, name='vote_result'),
    # url(r'^login/(?P<gender>\w+)/(?P<mate_date>\w+)/(?P<phoneNumber>\w+)/(?P<password>\d+)/$', views.login, name='login'),
    url(r'^login', views.login, name='login'),
    # url(r'^$', views.post_list, name='post_list'),
    # url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    # url(r'^post/new/$', views.post_new, name='post_new'),
    # url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    # url(r'^logout/', auth_views.logout,name='logout',kwargs={'template_name': 'blog/logout.html'}),
]


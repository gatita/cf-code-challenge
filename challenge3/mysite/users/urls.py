from django.conf.urls import patterns, url
from users import views

urlpatterns = patterns('',
    url(r'^create/$', views.create, name='create'),
    # url(r'^(?P<user_id>\d+)/edit/$', views.edit, name='edit'),
    # url(r'^(?p<user_id>\d+)/delete/$', views.delete, name='delete'),
    url(r'^$', views.user_list, name='user_list'),
    )
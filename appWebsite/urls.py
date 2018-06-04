from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^courses$', views.courses, name='courses'),
    url(r'^courses_detail(?P<pk>\d+)$', views.courses_detail, name='courses_detail'),
	url(r'^aboutus$', views.aboutus, name='aboutus'),
	url(r'^contactus$', views.contactus, name='contactus'),
	url(r'^offers$', views.offers, name='offers'),
    #   url(r'^courses/(?P<pk>\d+)/$', views.home, name='courses'),
#    url(r'^aboutus/(?P<pk>\d+)/$', views.home, name='aboutus'),
#  url(r'^contactus/(?P<pk>\d+)/$', views.home, name='contactus'),
#  url(r'^offers/(?P<pk>\d+)/$', views.home, name='offers'),
]
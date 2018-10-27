"""
URL Configuration

"""

from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^core/', include('core.urls')),
	url(r'', include('website.urls')),
]

# 2018.10.24-DEA

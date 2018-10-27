from django.conf.urls import url

from . import views

# Application Routes (URLs)

app_name = 'core'

urlpatterns = [

	# Login
	url(r'^auth/login/$', views.login, name='login'),

	# Logout
	url(r'^auth/logout/$', views.logout, name='logout'),
]

# 2018.10.24-DEA

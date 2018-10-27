from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, authenticate as auth_authenticate, logout as auth_logout
from django.conf import settings
from django.core.exceptions import SuspiciousOperation

from .utils import recaptcha_validation

# Application Views

# Login
def login(request):
	if (request.method == "POST"):
		if recaptcha_validation(request.POST.get('g-recaptcha-response')):
			form = AuthenticationForm(request, request.POST)
			if form.is_valid():
				username = form.cleaned_data.get('username')
				raw_password = form.cleaned_data.get('password')
				user = auth_authenticate(username=username, password=raw_password)
				auth_login(request, user)
				next_page = request.GET.get('next', 'website:home_page')
				return redirect(next_page)
		else:
			raise SuspiciousOperation()
	else:
		form = AuthenticationForm()

	context = { 'form': form, 'recaptcha_site_key': settings.RECAPTCHA_SITE_KEY }
	return render(request, 'registration/login_page.html', context)

# Logout
def logout(request):
	auth_logout(request)
	next_page = request.GET.get('next', 'website:home_page')
	return redirect(next_page)

# 2018.10.24-DEA

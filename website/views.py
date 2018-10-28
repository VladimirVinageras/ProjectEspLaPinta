from django.shortcuts import render, get_object_or_404 
from .models import Article, MenuElement
import datetime

def home(request):
	homeArticle = Article.objects.get(title="Home")
	allCourseArticles = Article.objects.filter(category='Course')
	allOpinionArticles = Article.objects.filter(category='Opinion')
	navItems = MenuElement.objects.all()
	year = datetime.datetime.now().year
	return render(request, 'website/home.html', {'homeArticle':homeArticle, 'navItems':navItems, 'allCourseArticles': allCourseArticles , 'allOpinionArticles': allOpinionArticles, 'year': year})


def courses(request):
	#homeArticle = Article.objects.get(title="Home")
	allCourseArticles = Article.objects.filter(category='Course')
	allOpinionArticles = Article.objects.filter(category='Opinion')
	navItems = MenuElement.objects.all()
	year = datetime.datetime.now().year
	return render(request, 'website/courses.html', {'navItems':navItems, 'allCourseArticles': allCourseArticles , 'allOpinionArticles': allOpinionArticles, 'year': year})

def aboutus(request):
	aboutusArticle = Article.objects.get(title="Aboutus")
	allOpinionArticles = Article.objects.filter(category='Opinion')
	navItems = MenuElement.objects.all()
	year = datetime.datetime.now().year
	return render(request, 'website/aboutus.html', {'aboutusArticle':aboutusArticle, 'navItems':navItems, 'allOpinionArticles': allOpinionArticles, 'year': year})

def contactus(request):
	contactusArticle = Article.objects.get(title="contactus")
	navItems = MenuElement.objects.all()
	year = datetime.datetime.now().year	
	return render(request, 'website/contactus.html', {'contactusArticle':contactusArticle, 'navItems':navItems, 'year': year})

def offers(request):
	offersArticle = Article.objects.get(title="offers")
	navItems = MenuElement.objects.all()
	allCourseArticles = Article.objects.filter(category='Course')
	year = datetime.datetime.now().year
	return render(request, 'website/offers.html', {'offersArticle':offersArticle, 'navItems':navItems, 'allCourseArticles': allCourseArticles, 'year': year})

def courses_detail(request, pk):
	article = get_object_or_404(Article, pk = pk)
	navItems = MenuElement.objects.all()
	year = datetime.datetime.now().year	
	allOpinionArticles = Article.objects.filter(category='Opinion')
	toCourseArticles = Article.objects.filter(category='Course')
	restCourseArticles = toCourseArticles.exclude(pk = pk)
	return render(request, 'website/courses_detail.html', {'article': article, 'navItems':navItems,'allOpinionArticles': allOpinionArticles, 'year': year, 'restCourseArticles': restCourseArticles})

#def base_Menu_Nav(request):
#
#	navItems = MenuElement.objects.all()
#
#	return render(request, 'website/home.html', {'navItems':navItems})
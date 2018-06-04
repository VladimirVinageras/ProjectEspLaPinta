from django.db import models
from django.utils import timezone




class Article(models.Model):
	title = models.CharField(max_length=200)
	text = models.TextField()
	photoUrl = models.CharField(max_length=1024)
	text_preview = models.TextField(default="Put your preview text here")
	text_intro = models.TextField(default="Put your preview text here")
	category = models.CharField(max_length=200)
	order = models.IntegerField()
	date_creation = models.DateTimeField(default=timezone.now)

	def get_Title(self):
		return self.title

	def get_Text(self):
		return self.text

	def get_PhotoURL(self):
		return self.photoUrl

	def get_TextPreview(self):
		return self.text_preview

	def get_TextIntro(self):
		return self.text_intro
	def get_order(self):
		return self.order

	



class Opinion(models.Model):
	student_name = models.CharField(max_length=200)
	student_photoURL = models.URLField()
	opinion = models.TextField()


class MenuElement(models.Model):
	name = models.CharField(max_length=200)
	url_link = models.CharField(max_length=256,default="Url here")
	level = models.IntegerField()
	position = models.IntegerField()
	#parent_element = models.ForeignKey('MenuElement')

	def get_name(self):
		return self.name

	def get_URLLink(self):
		return self.url_link

	def get_level(self):
		return self.level

	#def get_parent_element(self):
	#	return self.parent_element



# Create your models here.

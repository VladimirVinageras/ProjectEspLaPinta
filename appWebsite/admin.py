from django.contrib import admin
from .models import Article, Opinion, MenuElement


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title']
    ordering = ['title']


class MenuElementAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['position']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Opinion)
admin.site.register(MenuElement, MenuElementAdmin)




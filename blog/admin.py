# -*- coding:utf-8 -*-
from django.contrib import admin

from form import ArticleForm
from models import Article, Category


# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'alias', 'create_at')
    search_fields = ('name', 'alias')


class ArticleAdmin(admin.ModelAdmin):
    form = ArticleForm
    list_display = ('title', 'abstract', 'content', 'category', 'tags')
    search_fields = ('title', 'tags', 'abstract', 'content')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)

# -*- coding:utf-8 -*-
import json

from django.shortcuts import render
from django.views.generic.dates import MonthArchiveView
from .models import Article, Category


# Create your views here.
def get_archive():
    articles = Article.objects.all()
    year_month = set()
    for _article in articles:
        year_month.add((_article.create_at.year, _article.create_at.month))
    return year_month


def get_category():
    category_lists = Category.objects.all()
    category_lists = [category_list.data for category_list in category_lists]

    return category_lists


def get_recent_lists():
    recent_lists = Article.objects.all().filter(status=True).order_by('-create_at')[0:5]
    recent_lists = [recent_list.data for recent_list in recent_lists]

    return recent_lists


ARCHIVE = get_archive()
CATEGORY = get_category()
RECENT_LISTS = get_recent_lists()


def home(request):
    article_lists = Article.objects.all().filter(status=True).order_by('-create_at')
    article_lists = [article_list.data for article_list in article_lists]

    data = {
        'article_lists': article_lists,
        'recent_lists': RECENT_LISTS,
        'category_lists': CATEGORY,
        'archive_lists': ARCHIVE,
    }
    return render(request, 'home.html', data)


def blog(request):
    article_lists = Article.objects.all().filter(status=True).order_by('-create_at')
    article_lists = [article_list.data for article_list in article_lists]

    data = {
        'article_lists': article_lists,
    }
    return render(request, 'blog.html', data)


def article(request, pk):
    _article = Article.objects.get(pk=pk).data

    data = {
        'article': _article,
        'recent_lists': RECENT_LISTS,
        'category_lists': CATEGORY,
    }
    return render(request, 'article.html', data)


def category(request, category_id):
    article_lists = Article.objects.all().filter(status=True, category_id=category_id)
    article_lists = [article_list.data for article_list in article_lists]

    data = {
        'article_lists': article_lists,
        'recent_lists': RECENT_LISTS,
        'category_lists': CATEGORY,
    }
    return render(request, 'home.html', data)


# def search(request):
#     text = SearchForm(request.GET.get())
#     results = text.search()
#     # results = [results.data for result in results]
#     return render(request, 'search/search.html', {
#         'results': results,
#     })


class ArticleMonthArchiveView(MonthArchiveView):
    queryset = Article.objects.all()
    date_field = 'create_at'
    allow_future = True
    template_name = 'article_archive_month.html'

    def get_context_data(self, **kwargs):
        kwargs['recent_lists'] = RECENT_LISTS
        kwargs['category_lists'] = CATEGORY
        kwargs['archive_lists'] = ARCHIVE
        return super(MonthArchiveView, self).get_context_data(**kwargs)


def about(request):
    return render(request, 'about.html', {})


def contact(request):
    return render(request, 'contact.html', {})


def test(request):
    message = ['this a message']
    data = {
        'messages': message,
    }
    return render(request, 'test.html', data)

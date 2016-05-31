import haystack
from django.conf.urls import include, patterns, url
from django.contrib import admin

from blog.views import about, article, blog, category, contact, home, test
from settings import STATIC_PATH

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lofter.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls), name='admin'),
    url(r'^', include('django.contrib.auth.urls')),

    url(r'^$', home, name='home'),
    url(r'^home$', home, name='home'),

    url(r'^blog/$', blog, name='blog'),
    url(r'^article/(?P<pk>[0-9]+)/$', article, name='article'),
    url(r'^contact$', contact, name='contact'),
    url(r'^about$', about, name='about'),

    url(r'^search/', include('haystack.urls'), name='search'),
    url(r'^category/(?P<category_id>[0-9]+)/$', category, name='category'),

    # url(r'^category$', category, name='category'),
    # url(r'^message_board$', views.message_board, name='message board'),
    # url(r'^api/message_submit$', views.message_submit, name='message_submit'),

    url(r'^test$', test, name='test'),

    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': STATIC_PATH}),
)

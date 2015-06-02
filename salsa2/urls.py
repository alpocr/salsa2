from django.conf.urls import patterns, include, url
from django.conf import settings

from core.views import AddBookToCalendar, RecordList

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'salsa2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'core.views.home', name='home'),
    url(r'^calendar/', 'core.views.calendar', name='calendar'),
    url('^accounts/', include('django.contrib.auth.urls')),
    url(r'^record/add$', AddBookToCalendar.as_view(), name='add-book-to-calendar'),
    url(r'^list/$', RecordList.as_view(), name='record-list'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gtd.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^report/$', 'todo.views.index'),
    url(r'^report/(?P<item_id>[0-9]+)/complete/$', 'todo.views.complete_item'),
    url(r'^report/(?P<item_id>[0-9]+)/delete/$', 'todo.views.delete_item'),
    url(r'^report/add/$', 'todo.views.add_item'),
)

from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from ohrockman import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.index, name='index'),
    #url(r'^$', views.maintainence, name='maintainence'),
    url(r'^familytree/', include('familytree.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

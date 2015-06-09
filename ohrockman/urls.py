from django.conf.urls import patterns, include, url
from django.contrib import admin

from ohrockman import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ohrockman.views.home', name='home'),
    url(r'^/', include('familytree.urls')),
    url(r'^$', views.index, name='index'),
    #url(r'^$', views.maintainence, name='maintainence'),
    url(r'^familytree$', views.family_member, {'member_id':1}),
    url(r'^familytree/(?P<member_id>\d+)/$', views.family_member),
    url(r'^familytree/search', views.family_member_search),
    url(r'^reunion/$', views.reunion),
    #url(r'^gallery/$', views.gallery),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^photologue/', include('photologue.urls', namespace="photologue")),
)

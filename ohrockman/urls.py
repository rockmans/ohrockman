from django.conf import settings
from django.conf.urls import patterns, include, url, handler404, handler500
from django.conf.urls.static import static


from django.contrib import admin
admin.autodiscover()


from ohrockman import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       #url(r'^$', views.maintainence, name='maintainence'),
                       url(r'^familytree$', views.family_member, {'member_id':1}),
                       url(r'^familytree/(?P<member_id>\d+)/$', views.family_member),
                       
                       
                       url(r'^familytree/search', views.family_member_search),
                       url(r'^reunion/$', views.reunion),
                       url(r'^admin/', include(admin.site.urls)),
)

from django.conf.urls.defaults import *
from mysite.books import views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from views import *
urlpatterns = patterns('',
    ('^hello/$', hello),
    ('^display_meta/$',display_meta),
    (r'^search-form/$', views.search_form),
    (r'^search/$', views.search),
    (r'^test1-form/$', views.test1_form),
    (r'^test1/$', views.test1),
    # Example:
    # (r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),
)

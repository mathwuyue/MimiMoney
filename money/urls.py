from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'money.views.home', name='home'),
    # url(r'^money/', include('money.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
                       url(r'^main/', 'main.views.main'),
                       url(r'^shopping/', 'shopping.views.Shopping'),
                       url(r'^login/', 'account.views.userLogin'),
                       url(r'^users/', 'account.views.createUser'),
                       url(r'^(?P<path>.*)$', 'django.views.static.serve', {'document_root' : r'/home/wuyue/Projects/money'}),
)

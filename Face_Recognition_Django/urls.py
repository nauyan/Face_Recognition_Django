from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'Face_Recognition_Django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^model/', include('model.url')),
    url(r'^admin/', include(admin.site.urls)),
    
]

from django.conf.urls import include, url

urlpatterns = [
    url(r'^detect/', 'model.views.detect', name = 'detect'),
]

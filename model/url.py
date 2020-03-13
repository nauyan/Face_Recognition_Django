from django.conf.urls import include, url

urlpatterns = [
    url(r'^hello/', 'model.views.hello', name = 'hello'),
    url(r'^detect/', 'model.views.detect', name = 'detect'),
]

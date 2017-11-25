from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.plato_nuevo, name='plato_nuevo'),
    ]

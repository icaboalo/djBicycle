from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'bicycle/$', BicycleView.as_view()),
    url(r'bicycle/(?P<pk>[0-9]+)/$', BicycleDetailView.as_view()),
]
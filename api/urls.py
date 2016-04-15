from django.conf.urls import url
from .views import *
from rest_framework.authtoken import views as token_view

urlpatterns = [
    url(r'^token-auth/', token_view.obtain_auth_token),

    url(r'bicycle/$', BicycleView.as_view()),
    url(r'bicycle/(?P<pk>[0-9]+)/$', BicycleDetailView.as_view()),
]
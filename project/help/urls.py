# from django.contrib import admin
# from django.urls import path
from django.conf.urls import url
from help import views

urlpatterns = [
    url(r'^$', views.index)
]

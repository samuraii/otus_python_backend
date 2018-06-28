from django.conf.urls import url
from courses import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'python-one', views.python_one)
]

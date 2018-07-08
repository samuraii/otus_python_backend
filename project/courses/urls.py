from django.conf.urls import url
from courses import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'/*', views.course_page)
]

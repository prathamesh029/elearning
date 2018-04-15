from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index ,name='index'),
    url(r'^contact/', views.contact ,name='contact'),
    url(r'^PROGRAMMING/', views.PROGRAMMING ,name='PROGRAMMING'),
    url(r'^callme/', views.callme ,name='callme'),
     url(r'^cpp/', views.cpp ,name='cpp'),
     url(r'^javaa/', views.javaa ,name='javaa'),
     url(r'^PYTHONN/', views.PYTHONN ,name='PYTHONN'),
    ]

# Create your views here.s

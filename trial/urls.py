from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    path('', views.index, name='index'),
    path('sem/<student_roll>/<sem>/', views.sem, name='sem'),
    url(r'^marks/', views.test, name='marks')
]
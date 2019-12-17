"""p URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from trial import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('trial.urls')),
    path('trial/', include('trial.urls')),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='trial/login.html'), name='login'),
    url(r'^settings/myaccount/$', views.myaccount, name='myaccount'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^settings/password/$', auth_views.PasswordChangeView.as_view(template_name='trial/password_change.html'),
        name='password_change'),
    url(r'^settings/password/done/$', auth_views.PasswordChangeDoneView.as_view(template_name='trial/password_change_done.html'),
        name='password_change_done'),
]
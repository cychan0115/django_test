"""django_test1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include, url

import django1.views
urlpatterns = [
    url(r'^admin/' , admin.site.urls),
    url(r'^add/$',django1.views.add),
    url(r'^add/(\d+)/(\d+)/$',django1.views.add2 ),
    url(r'^home/',django1.views.home),
    url(r'^cytest/',django1.views.index),
    #url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^testdb_add/',django1.views.testdb),
    url(r'^testdb_select/',django1.views.testdb_select),
]
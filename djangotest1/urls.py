"""djangotest1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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

urlpatterns = [
	url(r'^$', 'blog.views.post_list', name='post_list'),
	url(r'^post/(?P<pk>\d+)/$', 'blog.views.post_detail', name = 'post_detail'),
	url(r'^about/$', 'blog.views.about', name='about'),
	url(r'^post/new/$', 'blog.views.post_new', name='post_new'),
	url(r'^post/(?P<pk>\d+)/edit/$', 'blog.views.post_edit', name='post_edit'),
    url(r'^admin/', admin.site.urls, name='admin_panel'),
]
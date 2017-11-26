from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [

    url(r'^$', TemplateView.as_view(template_name='blog/index.html'), name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'blog/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'blog/index.html'}, name='logout'),
]

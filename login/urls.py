from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.views import login, logout

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index')
]

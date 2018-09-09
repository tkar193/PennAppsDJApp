from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views.generic import View, TemplateView
from django.contrib.auth.decorators import permission_required

class IndexView(TemplateView):
    template_name = 'login/index.html'

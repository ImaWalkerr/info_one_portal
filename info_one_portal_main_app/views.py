from django import views
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .models import *


class MainPageView(TemplateView):
    template_name = 'index.html'

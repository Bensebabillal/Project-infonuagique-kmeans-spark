from django.shortcuts import render
from django.views.decorators.cache import never_cache
from django.views.generic import TemplateView

# Serve Vue Application
index_view = never_cache(TemplateView.as_view(template_name='index.html'))


def home_view(request):
    # render function takes argument  - request
    # and return HTML as response
    return render(request, "home.html")


def analysis_view(request):
    # render function takes argument  - request
    # and return HTML as response
    return render(request, "analysis.html")


def data_view(request):
    # render function takes argument  - request
    # and return HTML as response
    return render(request, "data.html")

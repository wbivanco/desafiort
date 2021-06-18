from django.shortcuts import render

from .services import get_sellers_by_category


def home(request):
    tenmplate_name = "home.html"

    return render(request, tenmplate_name, {})


def ranking_sellers(request):
    template_name = "sellers_list.html"

    params = {  }

    import json

    data = get_sellers_by_category(params)

    context = {
        'res': data
    }

    return render(request, template_name, context)
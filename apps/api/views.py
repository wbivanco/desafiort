from django.shortcuts import render

from .services import get_sellers_by_category, get_publishings_more_expensive


def home(request):
    tenmplate_name = "home.html"

    return render(request, tenmplate_name, {})


def ranking_publishings(request):
    template_name = "publishings_list.html"

    params = { }

    data = get_publishings_more_expensive(params)

    context = {
        'res': data
    }

    return render(request, template_name, context)


def ranking_sellers(request):
    template_name = "sellers_list.html"

    params = { }

    data = get_sellers_by_category(params)

    context = {
        'res': data
    }

    return render(request, template_name, context)
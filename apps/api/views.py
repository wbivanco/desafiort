from django.shortcuts import render

from .services import get_category


def ranking_sellers(requests):
    template_name = "sellers_list.html"

    params = { 'order': 'desc' }

    context = {
        'name': get_category(params)
    }

    return render(requests, template_name, context)
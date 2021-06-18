from django.shortcuts import render

from .services import get_sellers_by_category


def ranking_sellers(request):
    template_name = "sellers_list.html"

    params = {  }

    import json

    data = get_sellers_by_category(params)

    context = {
        'res': data
    }

    return render(request, template_name, context)
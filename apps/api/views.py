from django.shortcuts import render

from .services import get_sellers_by_category, get_publishings_more_expensive


def home(request):
    """
    Muestra ver la pantalla de inicio con el menú principal.
    """

    tenmplate_name = "home.html"

    return render(request, tenmplate_name, {})


def ranking_publishings(request):
    """
    Muestra el listado de los 5 vendedores que más vendieron en la categoría MLA352679
    """

    template_name = "publishings_list.html"

    params = { }

    data = get_publishings_more_expensive(params)

    context = {
        'res': data
    }

    return render(request, template_name, context)


def ranking_sellers(request):
    """
    Muestra el listado de la 20 punlicaciones más caras en la categoría MLA352679
    """

    template_name = "sellers_list.html"

    params = { }

    data = get_sellers_by_category(params)

    context = {
        'res': data
    }

    return render(request, template_name, context)
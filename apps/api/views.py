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
    Muestra el listado de la 20 publicaciones más caras en la categoría MLA352679
    """

    template_name = "publishings_list.html"

    data = []
    row = {}

    publishings = get_publishings_more_expensive()
    data_results = publishings.get('results')

    for result in data_results:
        row['titulo'] = result.get('title')
        row['precio'] = result.get('price')
        row['enlace'] = result.get('permalink')
        data.append(row.copy())

    context = {
        'res': data[:20]
    }

    return render(request, template_name, context)


def ranking_sellers(request):
    """
    Muestra el listado de los 5 vendedores que más vendieron en la categoría MLA352679
    """

    template_name = "sellers_list.html"

    publishings = get_sellers_by_category()
    data_results = publishings.get('results')

    seller_ids = []

    for result in data_results:
        seller_id = result.get('seller').get('id')
        if seller_id not in seller_ids:
            seller_ids.append(seller_id)

    context = {
        'res': seller_ids,
    }

    return render(request, template_name, context)
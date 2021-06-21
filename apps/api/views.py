from django.shortcuts import render

from .services import get_sellers_by_category, get_publishings_more_expensive, get_info_seller


#code = TG-60d0901838a5a4000780805f-85614757

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

    data = []  # Guardo las publicaciones en una lista que sera pasada al template
    row = {}  # Guardo el contentido de cada publicación en un diccionario con una estructura que solo contiene los
    # datos soliccitados y que formará parte de la lista de resultados

    publishings = get_publishings_more_expensive()  # Traigo info de la categoría y sus publicaciones ordenadas por
    # precio mas caro
    data_results = publishings.get('results')  # Obtengo solo los datos de las publicaciones.

    # Recorro cada publicación y cargo solo los datos en la lista que será utilizada en el template
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

    data_results = []  # Guarda todas las publicaciones de la categoría MLA352679

    # Este for me permite ir iterando en las publicaciones de la categoría para solo guardar en la lista los ids únicos
    # de cada vendor
    for i in range(0, 1000, 50):  # Hago for para ir pasando de pagina de a 50

        publishings = get_sellers_by_category(i)  # Traigo info de la categoría pasando un nuevo valor de offset en
        # cada iteración, es decir voy saltando de a 50 registros

        data_results.extend(publishings.get('results'))  # Guardo solo el conjunto de publicaciones obtenidas

    seller_ids = []  # Guardo los id no repetidos(únicos) de los vendedores de la categoría.

    # Este for me permite ir almacenando los id de los vendedores pero dichos id no deben estar repetidos
    for result in data_results:  # Itero en cada publicación

        seller_id = result.get('seller').get('id')  # Obtengo el id del vendedor de la publicación

        if seller_id not in seller_ids:  # Verifico si id esta en la lista, sino no esta agrego el id
            seller_ids.append(seller_id)

    seller = {}  # Almaceno los datos de un vendedor
    ranking_sellers = []  # Almaceno los datos de los vendedores que se van a mostar en el template

    # Con este for traigo toda la info del vendedor
    for seller_id in seller_ids:

        info_seller = get_info_seller(seller_id)  # Obtengo los datos (en ellos las publicaciones) de un vendedor en la
        # categoría MLA352679

        seller['nickname'] = info_seller.get('seller').get('nickname')

        pubs = info_seller.get('results')  # Obtengo las publicaciones del vendedor en la categoría MLA352679

        # sold_total = 0
        # for pub in pubs:
        #     sold_total = sold_total + pub.get('sold_quantity')
        # seller['sold_total'] = sold_total

        seller['sold_total'] = sum(item["sold_quantity"] for item in pubs)  # Sumo el total de lo vendido en cada
        # publacición y lo almaceno como total del vendedor en la categoría MLA352679
        ranking_sellers.append(seller.copy())

    sorted_ranking = sorted(ranking_sellers, key=lambda x: x['sold_total'], reverse=True)  # Con los totales de los
    # vendedores en la categoría, procedo a ordenar de mayor cantidad vendida a mennor

    context = {
        'res': sorted_ranking[:5],
    }

    return render(request, template_name, context)

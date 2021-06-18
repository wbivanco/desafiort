from django.urls import path

from .views import home, ranking_sellers, ranking_publishings

urlpatterns = [
    path('', home, name='home'),
    path('ranking_sellers/', ranking_sellers, name='ranking_sellers'),
    path('ranking_publishings/', ranking_publishings, name='ranking_publishings'),
]
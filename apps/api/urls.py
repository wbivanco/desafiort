from django.urls import path

from .views import home, ranking_sellers, ranking_publishings, get_category

urlpatterns = [
    path('', home, name='home'),
    path('ranking_sellers/', ranking_sellers, name='ranking_sellers'),
    path('ranking_publishings/', ranking_publishings, name='ranking_publishings'),
    path('connect_ml/', get_category, name='connect_ml'),
]
from django.urls import path

from .views import home, ranking_sellers

urlpatterns = [
    path('', home, name='home'),
    path('ranking_sellers/', ranking_sellers, name='ranking_sellers'),
]
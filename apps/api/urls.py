from django.urls import path

from .views import ranking_sellers

urlpatterns = [
    # Medicos
    path('ranking_sellers/', ranking_sellers, name='ranking_sellers'),
]
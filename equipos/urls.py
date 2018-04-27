from django.urls import path
from equipos.views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('equipos/search/', search_result, name='searchresult'),
    path('equipos/<slug:slug>/', EquipoDetailView.as_view(), name='detail'),
    path('equipos/<slug:slug>/solicitud/', EquipoSolicitadoView.as_view(), name='solicitado'),
]

from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DetailView
from equipos.models import Equipo
from equipos.forms import SearchForm
from django.http import HttpResponseNotFound
from django.conf import settings

# Create your views here.

def search_result(request):
    form = SearchForm(request.POST)

    if form.is_valid():
        resultSearch = form.save(commit=False)
        queryResult = resultSearch.tipo
        equipos = Equipo.objects.filter(title_icontains=queryResult)
        return render(request, 'equipos/search.html', {'equipos':equipos,'queryResult':queryResult})
    else:
        return HttpResponseNotFound('La busqueda es incorrecta')

class HomeView(TemplateView):
    template_name = 'equipos/home.html'

    def get_context_data(self, *args, **kwargs):
        search_form = SearchForm()
        equipos = Equipo.objects.all()
        return {'equipos':equipos, 'search_form': search_form}

class EquipoDetailView(DetailView):
    model = Equipo

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context

class EquipoSolicitadoView(DetailView):
    model = Equipo
    template_name = 'equipos/solicitud.html'

    def post(self, request, *args, **kwargs):
        equipo = self.get_object()
        error_message = None
        return render(request, 'equipos/revisado.html', {'equipo': equipo})

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',include('equipos.urls')),
    path('admin/', admin.site.urls),
    #path('estudiantes/', include('estudiantes.urls', namespace='estudiantes')),

]

from django.urls import path
from . import views

urlpatterns = [
    path('createequipo/', views.CreateEquipoView.as_view(), name='equipo_form')
]

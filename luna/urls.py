from django.urls import path
from . import views
from django.contrib.auth.views import logout_then_login,redirect_to_login

urlpatterns = [
    path('',views.home, name="home"),
    path('/servicio',views.servicio, name="servicio"),
    path('/registro',views.registro, name="registro"),
    path('/agendar/',views.agendar, name="agendar"),
    path('/profile/<id>',views.profile, name="profile"), 
    path('/eliminar/<id>/',views.eliminar_servicio, name="eliminar"),
    path('/modificar/<id>/',views.modificar_solicitud, name="modificar")
    
]
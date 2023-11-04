
from django.urls import path , include
from django.contrib import admin
from .views import saludo, resgistroPaciente, resgistroMedico, modificar, modificar2,modificarMedico,modificarMedico2,elimindarcli,registroContacto
from .views import saludo2, gestion, servicios, nosotros
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('',saludo, name="incicio"),
    path('saludo/',saludo2, name="paciente"),
    path('pacientesregistro/',resgistroPaciente, name="pacientes"),
    path('registromedico/',resgistroMedico, name="medicos"),
    path('editar/',modificar, name="modifi"),
    path('editar2/<id>/',modificar2, name="modifi_2"),
    path('editarmedico/',modificarMedico, name="modifiMe"),
    path('editarmedico2/<id>/',modificarMedico2, name="modifi_Me2"),
    path('deleteclie/<id>',elimindarcli,name="elimindar1"),
    path('contacto/',registroContacto,name="contactar"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('gestion/',gestion, name="gestion"),
    path('servicios/',servicios, name="servi"),
    path('nosotros/',nosotros, name="nosotro"),

]

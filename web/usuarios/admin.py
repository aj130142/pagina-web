from django.contrib import admin
from usuarios.models import Cliente, Especialidad, medico,contacto
# Register your models here.

class estiloClientes(admin.ModelAdmin):
    list_display= ['Nombre','DPI', 'Fecha_Actual','Tel']
    search_fields=['Nombre','DPI']

class estiloMedico(admin.ModelAdmin):
    list_display= ['Nombre','No_colegiado', 'Email','Tel']
    search_fields=['Nombre','No_colegiado']

class estiloEspecialidad(admin.ModelAdmin):
    list_display= ['nombre']
    search_fields=['nombre']

class estiloContacto(admin.ModelAdmin):
    list_display= ['Nombre','Asunto','Email']
    search_fields=['Nombre','Email']

admin.site.register(Cliente,estiloClientes)
admin.site.register(Especialidad,estiloEspecialidad)
admin.site.register(medico,estiloMedico,)
admin.site.register(contacto,estiloContacto)
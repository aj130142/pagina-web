from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.

def validate_dpi(value):
    if  value > 9999999999999:
        raise ValidationError('El valor del DPI debe estar en el 13.')
def validate_tel(value):
    if value > 99999999:
        raise ValidationError('El valor del DPI debe estar en el 8.')
def validate_cole(value):
    if value > 999999999:
        raise ValidationError('El valor del DPI debe estar en el 9.')

class Cliente(models.Model):
    Nombre = models.CharField(max_length=500)
    DPI = models.IntegerField(validators=[validate_dpi],unique=True)
    Nacimiento= models.CharField(max_length=10)
    Direccion = models.CharField(max_length=150)
    Razon= models.TextField(max_length=1000)
    Receta=models.ImageField()
    Tel = models.IntegerField(validators=[validate_tel])
    Email = models.EmailField(blank=True,null=True)
    Fecha_Actual= models.CharField(max_length=10)
    Nombre_Medico=models.CharField(max_length=500)

    
    def __str__(self):
        return "Paciente %s, DPI %s, fecha de entrada %s, telefono %s" % (self.Nombre, self.DPI, self.Fecha_Actual,self.Tel)
    
class Especialidad(models.Model):
    nombre = models.CharField(max_length=150)
    def __str__(self):
        return self.nombre

class medico(models.Model):
    Nombre = models.CharField(max_length=500)
    No_colegiado = models.IntegerField(validators=[validate_cole],unique=True)
    Especialidad= models.ForeignKey(Especialidad, on_delete=models.PROTECT)
    Diagnostico= models.TextField(max_length=1500)
    Tel = models.IntegerField(validators=[validate_tel])
    Email = models.EmailField(blank=True,null=True)
    Nombre_Paciente= models.CharField(max_length=500)
    def __str__(self):
        return "Medico %s, No de colegiado %s, direccion del correo %s, telefono %s" % (self.Nombre, self.No_colegiado, self.Email,self.Tel)

class contacto(models.Model):
    Nombre = models.CharField(max_length=500)
    Asunto = models.CharField(max_length=500)
    Email = models.EmailField()
    Razon= models.TextField(max_length=3500)
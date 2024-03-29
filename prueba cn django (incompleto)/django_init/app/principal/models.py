from django.db import models

class Empleado(models.Model):
    idEmpleado = models.AutoField(primary_key=True)
    idTipoEmpleado = models.IntegerField ()
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fechaNacimiento = models.DateField ()
    dni = models.CharField(max_length=10)
    sexo = models.CharField(max_length=10)
    telefono = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    localidad = models.CharField(max_length=50)
    provincia = models.CharField(max_length=50)
    grupoSanguineo = models.CharField(max_length=5)
    email = models.EmailField(max_length=50) 
    fechaIngreso = models.DateField ()
    usuario = models.CharField(max_length=50)
    contrasenia = models.CharField(max_length=50)
    observaciones = models.CharField(max_length=200)

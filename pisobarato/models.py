import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Piso (models.Model):
	OPCIONES_CHOICES = (
		('PISO', 'Piso'),
		('HABITACION', 'Habitacion')
	)
	id_piso = models.AutoField(primary_key=True)
	user = models.ForeignKey(User, blank=True, null=True)
	titulo = models.CharField (max_length=200, blank=True)
	tipo = models.CharField(max_length=10, choices=OPCIONES_CHOICES, default="PISO")
	lat = models.FloatField(null=True,default=0.0)
	lng = models.FloatField(null=True,default=0.0)
	descripcion = models.TextField ('Descripcion', blank=True)
	direccion = models.CharField (max_length=200, blank=True)
	fecha_registro = models.DateField ('Fecha registro', default=datetime.date.today)
	precio = models.FloatField(default=0.0)
	
	REQUIRED_FIELDS = ['user,titulo,direccion,precio,fecha_registro,descripcion']
	
	class Meta:
		verbose_name_plural = 'Pisos'
		ordering = ['id_piso']
	def __unicode__(self):
		return u"%s" % self.titulo

def get_img_url(instance, filename):
	return 'pisos/%d/%s' % (instance.id_piso.id_piso, filename)

class Imagen(models.Model):
	id_img = models.AutoField(primary_key=True)
	titulo = models.CharField (max_length=200, default='Titulo de la Imagen')
	id_piso = models.ForeignKey(Piso, blank=True, null=True)
	pic = models.ImageField(upload_to=get_img_url)
	class Meta:
		verbose_name_plural = 'Imagenes'
		ordering = ['id_piso']
	def __unicode__(self):
		return u"%s" % self.titulo

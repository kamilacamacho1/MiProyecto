from django.db import models
from django.contrib.auth.models import User



class Talla(models.Model):
	nombre = models.CharField(max_length = 6)

	def __unicode__ (self):
		return self.nombre

class Material(models.Model):
	nombre = models.CharField(max_length = 100)

	def __unicode__ (self):
		return self.nombre


class Modelo(models.Model):
	nombre = models.CharField(max_length = 100)

	def __unicode__ (self):
		return self.nombre


class Marca(models.Model):
	def url(self,filename):
		ruta = "MultimediaData/Marca/%s/%s"%(self.nombre, str(filename))
		return ruta

	nombre = models.CharField(max_length = 100)
	imagen = models.ImageField(upload_to = url, null = True, blank = True)

	def __unicode__ (self):
		return self.nombre


class Camiseta (models.Model):

	def url (self,filename):
		ruta = "MultimediaData/Producto/%s/%s"%(self.nombre, str(filename))
		return ruta

	nombre			= models.CharField(max_length = 100)
	descripcion     = models.TextField(max_length = 500)
	imagen			= models.ImageField(upload_to = url, null = True, blank =True)
	precio			= models.DecimalField(max_digits = 6, decimal_places = 2)
	stock			= models.IntegerField()
	modelo			= models.ManyToManyField(Modelo, null = True, blank = True)
	marca			= models.ForeignKey(Marca)
	talla			= models.ForeignKey(Talla)
	material		= models.ForeignKey(Material)



	def __unicode__ (self):
		return self.nombre


class user_profile(models.Model):

	def url(self,filename):
		ruta = "MultimediaData/users/%s/%s"%(self.user.username,filename)
		return ruta

	user = models.OneToOneField(User)
	photo = models.ImageField(upload_to=url)
	telefono =models.CharField(max_length=30)

	def __unicode__(self):
	 	return self.user.username
	

# Create your models here.
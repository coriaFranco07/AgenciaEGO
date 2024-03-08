import random
import string
from django.db import models
from django.utils.text import slugify



class Marca(models.Model):
    nombre = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, blank=True)  
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        
        if not self.slug:
            base_slug = slugify(self.nombre)
            random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
            object_id = str(self.id)
            self.slug = f"{base_slug}-{random_string}-{object_id}"
        super(Marca, self).save(*args, **kwargs)


    class Meta:
        verbose_name='marca'
        verbose_name_plural='marcas'

    def __str__(self):
        return self.nombre 
    

class Modelo(models.Model):
    año = models.IntegerField()
    slug = models.SlugField(unique=True, blank=True)  
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(str(self.año))  # Aquí estoy usando el año como base para el slug
            random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
            object_id = str(self.id)
            self.slug = f"{base_slug}-{random_string}-{object_id}"
        super(Modelo, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'modelo'
        verbose_name_plural = 'modelos'

    def __str__(self):
        return str(self.año)
    

class Auto(models.Model):

    nombre=models.CharField(max_length=50)
    marca=models.ManyToManyField(Marca) 
    modelo=models.ManyToManyField(Modelo) 

    imagen=models.ImageField(upload_to="auto", null=True, blank=True)
    dscAuto=models.CharField(max_length=500, default='Valor predeterminado')

    imagenMotor=models.ImageField(upload_to="auto", null=True, blank=True)
    dscMotor=models.CharField(max_length=500, default='Valor predeterminado')

    imagenVolante=models.ImageField(upload_to="auto", null=True, blank=True)
    dscVolante=models.CharField(max_length=500, default='Valor predeterminado')

    imagenPiston=models.ImageField(upload_to="auto", null=True, blank=True)
    dscPiston=models.CharField(max_length=500, default='Valor predeterminado')

    imagenMantenimiento=models.ImageField(upload_to="auto", null=True, blank=True)
    dscMantenimiento=models.CharField(max_length=500, default='Valor predeterminado')

    imagenNeumatico=models.ImageField(upload_to="auto", null=True, blank=True)
    dscNeumatico=models.CharField(max_length=500, default='Valor predeterminado')

    imagenEstructura=models.ImageField(upload_to="auto", null=True, blank=True)
    dscEstructura=models.CharField(max_length=500, default='Valor predeterminado')

    precio=models.FloatField()
    disponibilidad=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='auto'
        verbose_name_plural='autos'

    def __str__(self):
        return self.nombre 
    


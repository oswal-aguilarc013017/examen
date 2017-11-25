from django.db import models
from django.contrib import admin  #libreria de python


class Plato(models.Model):
    nombre = models.CharField(max_length=60)
    descripcion = models.CharField(blank=True, max_length=200)
    def __str__(self):
        return self.nombre

class Menu(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return self.nombre

class Union(models.Model):
    autor = models.ForeignKey('auth.User')
    plato = models.ForeignKey(Plato, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    def __str__(self):
        return self.menu.nombre

class UnionInLine(admin.TabularInline):
    model = Union
    extra = 1

class PlatoAdmin(admin.ModelAdmin):
    inlines = (UnionInLine,)

class MenuAdmin (admin.ModelAdmin):
    inlines = (UnionInLine,)

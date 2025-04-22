#models.py
from django.db import models

# Create your models here.

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    anio_publicacion = models.IntegerField()
    genero = models.CharField(max_length=100)
    fecha_registro = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Resena(models.Model):
    libro = models.ForeignKey(Libro, related_name='resenas', on_delete=models.CASCADE)
    usuario = models.CharField(max_length=100)
    comentario = models.TextField()
    calificacion = models.IntegerField()
    fecha = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('libro', 'usuario')  # el usuario podrá reseñar solamente un libro

    def __str__(self):
        return f"{self.usuario} - {self.libro.titulo}"

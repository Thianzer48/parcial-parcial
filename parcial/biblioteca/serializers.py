#serializers.py
from rest_framework import serializers
from .models import Libro, Resena

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = '__all__' #serializa todos los campos


class ResenaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resena
        fields = '__all__'

    def validate_calificacion(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("La calificación debe estar entre 1 y 5.")
        return value

    def validate(self, data):
        usuario = data.get('usuario')
        libro = data.get('libro')
        if Resena.objects.filter(libro=libro, usuario=usuario).exists():
            raise serializers.ValidationError("Este usuario ya ha hecho una reseña para este libro.")
        return data

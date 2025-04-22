#views.py
from rest_framework import generics
from .models import Libro, Resena
from .serializers import LibroSerializer, ResenaSerializer

# Libros
class LibroListCreate(generics.ListCreateAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

class LibroRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

# Reseñas
class ResenaListCreate(generics.ListCreateAPIView):
    serializer_class = ResenaSerializer

    def get_queryset(self):
        return Resena.objects.filter(libro_id=self.kwargs['libro_id'])

    def perform_create(self, serializer):
        libro_id = self.kwargs['libro_id']
        serializer.save(libro_id=libro_id)

class ResenaDelete(generics.DestroyAPIView):
    queryset = Resena.objects.all()
    serializer_class = ResenaSerializer

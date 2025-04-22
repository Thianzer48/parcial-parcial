#urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('libros/', views.LibroListCreate.as_view()),
    path('libros/<int:pk>/', views.LibroRetrieveUpdateDelete.as_view()),
    path('libros/<int:libro_id>/resenas/', views.ResenaListCreate.as_view()),
    path('resenas/<int:pk>/', views.ResenaDelete.as_view()),
]


# 📚 API RESTful de "Reseñoteca"

Este proyecto es una API RESTful desarrollada con Django y Django REST Framework para gestionar **libros** y sus respectivas **reseñas**. 
El objetivo es demostrar el diseño de modelos relacionados, validaciones, exposición de endpoints y consumo desde herramientas externas como Postman (aunque dio error y no se dejó usar 👺) 

---

## ⚙️ Tecnologías usadas

- Python 3
- Django
- Django REST Framework
- MySQL Workbench (por defecto)

---

## 🏗️ Estructura del Proyecto

- `Libro`: modelo principal que representa un libro.
- `Resena`: modelo secundario relacionado a un libro (uno a muchos).
- Endpoints para CRUD de libros y manejo de reseñas.

---

## 📁 Endpoints disponibles

> Todos los endpoints están bajo el prefijo `/api/`

### 📘 Libros

| Método | Endpoint                 | Descripción                        |
|--------|--------------------------|------------------------------------|
| GET    | `/api/libros/`           | Listar todos los libros            |
| POST   | `/api/libros/`           | Crear un nuevo libro               |
| GET    | `/api/libros/<id>/`      | Obtener detalles de un libro       |
| PUT    | `/api/libros/<id>/`      | Actualizar un libro existente      |
| DELETE | `/api/libros/<id>/`      | Eliminar un libro                  |

### ✍️ Reseñas

| Método | Endpoint                                 | Descripción                                |
|--------|------------------------------------------|--------------------------------------------|
| GET    | `/api/libros/<libro_id>/resenas/`        | Listar reseñas de un libro específico      |
| POST   | `/api/libros/<libro_id>/resenas/`        | Crear una nueva reseña para ese libro      |
| DELETE | `/api/resenas/<resena_id>/`              | Eliminar una reseña específica             |

---

## ✅ Validaciones importantes

- Un usuario solo puede hacer **una reseña por libro** (`validate_calificacion`).
- La **calificación** de una reseña debe estar entre **1 y 5**.

---

## 🚀 Cómo ejecutar el proyecto

1. Clonar el repositorio
2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt

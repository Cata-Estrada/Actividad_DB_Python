# 🐍 Proyecto Django: Colegio

## PASO 1. Crear entorno virtual e instalar Django
1. Abre terminal o consola.  
2. Crea un entorno virtual:  
    ```bash
   python -m venv venv
   ```
   
3. Actívalo:  
   - **En Windows:**  
     ```bash
     venv\Scripts\activate
     ```  
   - **En Linux/Mac:**  
     ```bash
     source venv/bin/activate
     ```  
    
4. Una vez dentro del entorno virtual, instala Django:  
```bash
pip install django
```
---

## PASO 2. Crear un nuevo proyecto Django

En terminal ejecuta:
    django-admin startproject colegio .


📌 **Observaciones**:  
- El `.` hace que **manage.py** se cree en la carpeta actual (raíz).  
- También se creará una subcarpeta `colegio/` con `settings.py`, `urls.py`, etc.  

---

## PASO 3. Crear la primera aplicación: **estudiante**
En la terminal:
    python manage.py startapp estudiante


Registrar la app en `settings.py`  
```python
INSTALLED_APPS = [
    ...,
    'estudiante',
]
```

### Definir el modelo Estudiante
En `estudiante/models.py`:
```python
from django.db import models

class Estudiante(models.Model):
    cedula = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    correo = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombre} ({self.cedula})"
```

---

## 4. Crear dos tablas adicionales en la app **estudiante**
En el mismo archivo `models.py`, agrega:
```python
class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class Nota(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    calificacion = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.estudiante.nombre} - {self.curso.nombre}: {self.calificacion}"
```

---

## 5. Crear dos apps adicionales

### 5.1 App **profesor**
```bash
python manage.py startapp profesor
```

En `settings.py` agrega `'profesor'`.  

En `profesor/models.py`:  
```python
from django.db import models

class Profesor(models.Model):
    cedula = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
```

---

### 5.2 App **materia**
```bash
python manage.py startapp materia
```

En `settings.py` agrega `'materia'`.  

En `materia/models.py`:  
```python
from django.db import models

class Materia(models.Model):
    nombre = models.CharField(max_length=100)
    creditos = models.IntegerField()

    def __str__(self):
        return self.nombre
```

---

## 6. Migraciones y base de datos
Ejecutar en la terminal:
```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 7. Activar el panel de administración

1. Crear un superusuario:
   ```bash
   python manage.py createsuperuser
   ```
   Completa con usuario, correo y contraseña.  

2. Registrar los modelos en el admin:  

`estudiante/admin.py`
```python
from django.contrib import admin
from .models import Estudiante, Curso, Nota

admin.site.register(Estudiante)
admin.site.register(Curso)
admin.site.register(Nota)
```

`profesor/admin.py`
```python
from django.contrib import admin
from .models import Profesor

admin.site.register(Profesor)
```

`materia/admin.py`
```python
from django.contrib import admin
from .models import Materia

admin.site.register(Materia)
```

---

## 8. Probar el proyecto
Iniciar el servidor:
```bash
python manage.py runserver
```

Abrir en el navegador:  
👉 [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

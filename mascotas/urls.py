from django.contrib import admin
from django.urls import path
from gestor import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.listar_mascotas, name='listar_mascotas'),
    path('crear/', views.crear_mascota, name='crear_mascota'),
    path('editar/<int:mascota_id>/', views.editar_mascota, name='editar_mascota'),
    path('eliminar/<int:mascota_id>/', views.eliminar_mascota, name='eliminar_mascota'),
]
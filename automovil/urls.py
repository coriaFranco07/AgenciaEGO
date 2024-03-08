from django.urls import path
from . import views

app_name = 'automovil'

urlpatterns = [

path('', views.auto, name="auto"),


path('ver-modelo/<int:pk>/', views.ver_modelo, name='ver_modelo'),



path('api/autos/', views.TodosLosAutosAPIView.as_view()),
path('traer/', views.mostrar_autos, name='todos-los-autos'),

path('editar_auto/<int:pk>/', views.editar_auto, name='editar'),
path('api/editar/<int:pk>/', views.EditarAutoAPIView.as_view(), name='editar_auto_api'),

path('crear_auto/', views.crear_auto, name='agregar'),
path('api/agregar/', views.CrearAutoAPIView.as_view(), name='crear_auto_api'),

path('api/eliminar/<int:pk>/', views.EliminarAutoAPIView.as_view(), name='eliminar_auto_api'),
path('api/modelos/<int:pk>/', views.ModeloDetailAPIView.as_view(), name='modelo-list'),
path('api/marcas/<int:pk>/', views.MarcaDetailAPIView.as_view(), name='marca-list'),





path('api/marcas/', views.MarcaListAPIView.as_view()),
path('traerMarcas/', views.mostrar_marcas, name='marcas'),

path('crear_marca/', views.crear_marca, name='agregarMarca'),
path('api/agregarMarca/', views.CrearMarcaAPIView.as_view(), name='crear_marca_api'),

path('editar_marca/<int:pk>/', views.editar_marca, name='editarMarca'),
path('api/editarMarca/<int:pk>/', views.EditarMarcaAPIView.as_view(), name='editar_marca_api'),





path('api/modelos/', views.ModeloListAPIView.as_view()),
path('traerModelos/', views.mostrar_modelos, name='modelos'),

path('crear_modelo/', views.crear_modelo, name='agregarModelo'),
path('api/agregarModelo/', views.CrearModeloAPIView.as_view(), name='crear_modelo_api'),

path('editar_modelo/<int:pk>/', views.editar_modelo, name='editarModelo'),
path('api/editarModelo/<int:pk>/', views.EditarModeloAPIView.as_view(), name='editar_modelo_api'),

]
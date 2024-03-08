from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
import requests
from automovil.models import Auto, Marca, Modelo

from django.http import HttpResponse
from django.template import loader
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Auto
from .serializers import AutoSerializer, MarcaSerializer, ModeloSerializer


# Create your views here.
from django.shortcuts import render
from .models import Auto, Marca, Modelo
import requests

def auto(request):
    # Consultar directamente a la base de datos para obtener los autos disponibles
    autos = Auto.objects.filter(disponibilidad=True)
    marcas = Marca.objects.all()  # Obtener todas las marcas desde la base de datos
    modelos = Modelo.objects.all()  # Obtener todos los modelos desde la base de datos

    # Obtener los parámetros de filtro y orden de la solicitud GET
    marca_seleccionada = request.GET.get('marca')
    modelo_seleccionado = request.GET.get('modelo')
    orden = request.GET.get('orden')

    # Filtrar los autos por marca si se proporciona un parámetro de marca en la solicitud GET
    if marca_seleccionada:
        autos = autos.filter(marca__slug=marca_seleccionada)

    # Filtrar los autos por modelo si se proporciona un parámetro de modelo en la solicitud GET
    if modelo_seleccionado:
        autos = autos.filter(modelo__slug=modelo_seleccionado)

    # Hacer una solicitud a la API para obtener información adicional sobre marcas y modelos
    response_marcas = requests.get('http://127.0.0.1:8000/autos/api/marcas/')
    response_modelos = requests.get('http://127.0.0.1:8000/autos/api/modelos/')
    
    # Obtener los datos de las marcas y modelos desde la API
    marcas_api = response_marcas.json()
    modelos_api = response_modelos.json()

    # Mapear los datos de la API a diccionarios para facilitar el acceso por ID
    marcas_dict = {marca['id']: marca['nombre'] for marca in marcas_api}
    modelos_dict = {modelo['id']: modelo['año'] for modelo in modelos_api}

    # Actualizar los nombres de las marcas y modelos en los autos
    for auto in autos:
        # Obtener el nombre de la marca del diccionario de marcas
        auto.marca_nombre = marcas_dict.get(auto.marca, 'Desconocido')
        # Obtener el año del modelo del diccionario de modelos
        auto.modelo_año = modelos_dict.get(auto.modelo, 'Desconocido')

    if orden == 'precio_asc':
        autos = autos.order_by('precio')  # Orden ascendente por precio
    elif orden == 'precio_desc':
        autos = autos.order_by('-precio')  # Orden descendente por precio
    elif orden == 'año_asc':
        autos = autos.order_by('modelo__año')  # Orden ascendente por año del modelo
    elif orden == 'año_desc':
        autos = autos.order_by('-modelo__año')  # Orden descendente por año del modelo

    # Pasar los autos y las marcas a la plantilla para su visualización
    return render(request, 'autos/auto.html', {'autos': autos, 'marcas': marcas, 'modelos': modelos})


def ver_modelo(request, pk):
    auto = get_object_or_404(Auto, pk=pk)

    # Obtener las marcas y modelos para pasar a la plantilla
    marcas = Marca.objects.all()
    modelos = Modelo.objects.all()

    # Hacer una solicitud a la API para obtener información adicional sobre marcas y modelos
    response_marcas = requests.get('http://127.0.0.1:8000/autos/api/marcas/')
    response_modelos = requests.get('http://127.0.0.1:8000/autos/api/modelos/')
    
    # Obtener los datos de las marcas y modelos desde la API
    marcas_api = response_marcas.json()
    modelos_api = response_modelos.json()

    # Mapear los datos de la API a diccionarios para facilitar el acceso por ID
    marcas_dict = {marca['id']: marca['nombre'] for marca in marcas_api}
    modelos_dict = {modelo['id']: modelo['año'] for modelo in modelos_api}

    # Actualizar los nombres de la marca y el año del modelo en el auto
    auto.marca.nombre = marcas_dict.get(auto.marca, 'Desconocido')
    auto.modelo.año = modelos_dict.get(auto.modelo, 'Desconocido')

    # Pasar el auto, las marcas y los modelos a la plantilla para su visualización
    return render(request, 'autos/detalleAuto.html', {'auto': auto, 'marcas': marcas, 'modelos': modelos})









class EliminarAutoAPIView(APIView):
    def delete(self, request, pk):
        try:
            auto = Auto.objects.get(pk=pk)
            auto.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Auto.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
class TodosLosAutosAPIView(APIView):
    def get(self, request):
        queryset = Auto.objects.all()
        serializer = AutoSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AutoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class MarcaDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            marca = Marca.objects.get(pk=pk)
        except Marca.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = MarcaSerializer(marca)
        return Response(serializer.data)

class ModeloDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            modelo = Modelo.objects.get(pk=pk)
        except Modelo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = ModeloSerializer(modelo)
        return Response(serializer.data)
    
def mostrar_autos(request):
    # Hacer una solicitud a tu API para obtener los autos
    response = requests.get('http://127.0.0.1:8000/autos/api/autos/')
    autos = response.json()

    # Obtener los nombres de las marcas y modelos correspondientes a cada auto
    for auto in autos:
        # Obtener los nombres de las marcas
        marca_ids = auto.get('marca', [])
        nombre_marcas = []
        for marca_id in marca_ids:
            # Hacer una solicitud a la API para obtener el detalle de la marca
            response = requests.get(f'http://127.0.0.1:8000/autos/api/marcas/{marca_id}/')
            marca = response.json()
            nombre_marca = marca.get('nombre', 'Desconocido')
            nombre_marcas.append(nombre_marca)
        # Actualizar el campo 'marca' del auto con los nombres de las marcas
        auto['marca'] = nombre_marcas

        # Obtener los nombres de los modelos
        modelo_ids = auto.get('modelo', [])
        año_modelos = []
        for modelo_id in modelo_ids:
            # Hacer una solicitud a la API para obtener el detalle del modelo
            response = requests.get(f'http://127.0.0.1:8000/autos/api/modelos/{modelo_id}/')
            modelo = response.json()
            añoo_modelo = modelo.get('año', 'Desconocido')
            año_modelos.append(añoo_modelo)
        # Actualizar el campo 'modelo' del auto con los nombres de los modelos
        auto['modelo'] = año_modelos

    return render(request, 'administrar/todosAutos.html', {'autos': autos})

def editar_auto(request, pk):
    auto = get_object_or_404(Auto, pk=pk)
    marcas = Marca.objects.all()
    modelos = Modelo.objects.all()
    return render(request, 'administrar/editarAuto.html', {'auto': auto, 'marcas': marcas, 'modelos': modelos})

class EditarAutoAPIView(APIView):
    def post(self, request, pk):
        auto = get_object_or_404(Auto, pk=pk)
        serializer = AutoSerializer(auto, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            # Redirigir al índice después de guardar exitosamente
            return redirect('automovil:todos-los-autos')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def crear_auto(request):
    marcas = Marca.objects.all()
    modelos = Modelo.objects.all()
    return render(request, 'administrar/agregarAuto.html', {'marcas': marcas, 'modelos': modelos})
    
class CrearAutoAPIView(APIView):
    def post(self, request):
        serializer = AutoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Redirigir al índice después de guardar exitosamente
            return redirect('automovil:todos-los-autos')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    




#Trabajando con Marcas

def mostrar_marcas(request):
    # Hacer una solicitud a tu API para obtener los autos
    response = requests.get('http://127.0.0.1:8000/autos/api/marcas/')
    marcas = response.json()
    print(marcas)
    return render(request, 'marcas/marca.html', {'marcas': marcas})

class MarcaListAPIView(APIView):
    def get(self, request):
        marcas = Marca.objects.all()
        serializer = MarcaSerializer(marcas, many=True)
        return Response(serializer.data)


def editar_marca(request, pk):
    marca = get_object_or_404(Marca, pk=pk)
    return render(request, 'marcas/editarMarca.html', {'marca': marca})

class EditarMarcaAPIView(APIView):
    def post(self, request, pk):
        marca = get_object_or_404(Marca, pk=pk)
        serializer = MarcaSerializer(marca, data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Redirigir al índice después de guardar exitosamente
            return redirect('automovil:marcas')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def crear_marca(request):
    return render(request, 'marcas/agregarMarca.html')
    
class CrearMarcaAPIView(APIView):
    def post(self, request):
        serializer = MarcaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('automovil:marcas')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    




#Trabajando con Modelos

def mostrar_modelos(request):
    # Hacer una solicitud a tu API para obtener los autos
    response = requests.get('http://127.0.0.1:8000/autos/api/modelos/')
    modelos = response.json()
    print(modelos)
    return render(request, 'modelos/modelo.html', {'modelos': modelos})

class ModeloListAPIView(APIView):
    def get(self, request):
        modelos = Modelo.objects.all()
        serializer = ModeloSerializer(modelos, many=True)
        return Response(serializer.data)


def editar_modelo(request, pk):
    modelo = get_object_or_404(Modelo, pk=pk)
    return render(request, 'modelos/editarModelo.html', {'modelo': modelo})

class EditarModeloAPIView(APIView):
    def post(self, request, pk):
        modelo = get_object_or_404(Modelo, pk=pk)
        serializer = ModeloSerializer(modelo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Redirigir al índice después de guardar exitosamente
            return redirect('automovil:modelos')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def crear_modelo(request):
    return render(request, 'modelos/agregarModelo.html')
    
class CrearModeloAPIView(APIView):
    def post(self, request):
        serializer = ModeloSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('automovil:modelos')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

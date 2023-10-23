# views.py
from django.shortcuts import render
from .forms import TableroForm


def index(request):
    return render(request, 'buscamina/index.html', {})


def tablero(request):
    if request.method == 'GET':
        form = TableroForm(request.GET)
        if form.is_valid():
            filas = form.cleaned_data['filas']
            columnas = form.cleaned_data['columnas']
            # Aquí puedes generar el tablero con las filas y columnas especificadas
            # y pasar los datos a la plantilla.
            tablero = crear_tablero(filas, columnas)
            return render(request, 'buscamina/crear_tablero.html', {'tablero': tablero})
    else:
        form = TableroForm()
    return render(request, 'buscamina/formulario.html', {'form': form})


def crear_tablero(filas, columnas):
    # Aquí puedes generar el tablero como una lista de listas o en el formato que necesites.
    # Por ejemplo, puedes usar un bucle para crear una lista de listas de celdas vacías.
    tablero = [['' for _ in range(columnas)] for _ in range(filas)]
    return tablero

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
            tablero = crear_tablero(filas, columnas)
            return render(request, 'buscamina/crear_tablero.html', {'tablero': tablero})
    else:
        form = TableroForm()
    return render(request, 'buscamina/formulario.html', {'form': form})


def crear_tablero(filas, columnas):
    tablero = [['' for _ in range(columnas)] for _ in range(filas)]
    return tablero

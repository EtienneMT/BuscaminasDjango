# forms.py
from django import forms


class TableroForm(forms.Form):
    filas = forms.IntegerField()
    columnas = forms.IntegerField()

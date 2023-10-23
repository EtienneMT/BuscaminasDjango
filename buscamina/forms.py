# forms.py
from django import forms


def validador_filas(value):
    if value < 0 or value > 20:
        raise forms.ValidationError("El valor debe estar entre 0 y 20.")


def validador_columnas(value):
    if value < 0 or value > 15:
        raise forms.ValidationError("El valor debe estar entre 0 y 15.")


class TableroForm(forms.Form):
    filas = forms.IntegerField(validators=[validador_filas])
    columnas = forms.IntegerField(validators=[validador_columnas])

from django import forms
from .models import Pokemon

#es un archivo donde puedes definir tus propios formularios personalizados utilizando la clase forms.ModelForm que proporciona Django.

class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = ('name', 'type', 'variable')


#La clase Meta es donde puedes definir los atributos del formulario. 
# En este caso, especificamos que el modelo a utilizar es Pokemon 
# y que los campos que queremos incluir en el formulario son name, type, y level.
# Con esto, ya tienes un archivo forms.py que define una clase de formulario 
# PokemonForm para tu modelo Pokemon. Ahora puedes utilizar esta clase 
# en tus vistas para mostrar formularios y validar datos de entrada del usuario.
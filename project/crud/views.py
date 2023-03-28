from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Pokemon
from .forms import PokemonForm

    # pokemon = Representa un objeto de la clase Pokemon definida en el archivo models.py
    # Pokemon = es el nombre de la clase en si misma!

def index(request): # lista de pokemons
    pokemons = Pokemon.objects.all()
    # que devuelve un QuerySet de todos 
    # los objetos de Pokemon en la base de datos.
    context = {'pokemons': pokemons}
    # plurar por qe esta es la lista 
    # Este diccionario se pasa como tercer parámetro al 
    # método render, que renderiza la plantilla 'index.html' 
    # con el contexto {'pokemons': pokemons}.  
    return render(request, 'index.html', {'pokemons': pokemons})
    # devuelve el resultado de la plantilla renderizada 
        # como una respuesta HTTP

def create(request): #función create que recibe un objeto request como parámetro.
    if request.method == 'POST': #verifica si el método de la solicitud HTTP es POST
        form = PokemonForm(request.POST)# crea una instancia de la clase PokemonForm con los datos del formulario enviados en la solicitud HTTP.
        if form.is_valid(): # verifica si el formulario es válido. En otras palabras, si se han proporcionado datos válidos y cumplen las restricciones definidas en el formulario.
            form.save() # guarda los datos proporcionados en el formulario en la base de datos.
            return redirect('index') # redirige al usuario a la vista index después de guardar los datos del formulario.
    else:
        form = PokemonForm() # crea una instancia de la clase PokemonForm sin ningún dato en caso de que el método de la solicitud HTTP no sea POST.
    context = {'form': form} #  crea un diccionario context que contiene el formulario creado en la línea anterior.
    return render(request, 'create.html', context) # enderiza la plantilla create.html con el diccionario context como contexto, creando así la página de creación de un nuevo Pokémon.

def details(request, pk): #detalle de un pokemon en singular
    pokemon = get_object_or_404(Pokemon, pk=pk) 
    # funcion proporcionada por Django toma argumento 1 el modelo a bu scar. 2 los argumentos para buscar el modelo, si no existe revuelve un 404 Not Found
    # es utilizada en una vista para recuperar un objeto de la base de datos que coincida con un cierto criterio. En este caso, se utiliza para recuperar un objeto Pokemon 
    # que tenga el atributo pk (clave primaria) igual al valor pasado como argumento en la URL.
    context = {'pokemon': pokemon}
    # crea un diccionario llamado context que contiene una sola clave-valor. La clave es 'pokemon' y su valor es el objeto pokemon que se obtuvo con la función get_object_or_404().
    # Este diccionario es utilizado para pasar datos a la plantilla de Django que se usará para renderizar la respuesta del servidor. En este caso, se está pasando el objeto pokemon a la 
    # plantilla para que pueda ser visualizado y accedido en la misma.
    return render(request, 'details.html', context)
    # se encarga de renderizar la plantilla HTML correspondiente al detalle de un Pokémon(details.html) con la información del Pokémon especificado en la URL a través de su id.

def edit(request, pk):
    pokemon = get_object_or_404(Pokemon, pk=pk) # Obtener el objeto Pokemon que queremos editar con get_object_or_404
    if request.method == 'POST':    #Si el método de la solicitud es POST, significa que el usuario ha enviado un formulario Así que creamos un formulario de PokemonForm con los datos 
                                    #recibidos en la solicitud (request.POST) y especificamos que deseamos actualizar el objeto "pokemon" existente.
        form = PokemonForm(request.POST, instance=pokemon)  #crea un formulario PokemonForm con los datos que se reciben en el request.POST y los datos de una instancia de pokemon. 
                                #El parámetro instance se utiliza para indicar que se quiere modificar una instancia existente de un modelo (pokemon en este caso), y no crear una nueva. 
                                #El formulario creado contendrá los datos de la instancia pokemon y se mostrará al usuario para que los edite o modifique.
        if form.is_valid():
            form.save() # guarda los datos proporcionados en el formulario en la base de datos.
            return redirect('index')
    else:
        # # 5. Si el método de la solicitud NO es POST, significa que el usuario acaba de acceder a la página de edición.
        #    Así que creamos un formulario de PokemonForm con la instancia del objeto "pokemon" que queremos editar
        #    y lo pasamos como argumento del contexto para que se muestren los valores existentes en el formulario.
        form = PokemonForm(instance=pokemon) #  instancia un objeto de la clase PokemonForm que representa un formulario para actualizar la información de un objeto Pokemon existente.
        # # 6. Creamos un diccionario "context" con el formulario "form" y el objeto "pokemon"
        #    (que queremos editar y que hemos pasado como argumento al formulario en el paso 5)
        #    Y luego, renderizamos el formulario "create.html" con el contexto y lo devolvemos como respuesta.
    context = {'form': form, 'pokemon': pokemon}
    #'form': form: el valor es el objeto form creado a partir de la clase PokemonForm. Este formulario se utiliza para mostrar los datos del pokemon en un formulario de edición en la plantilla HTML edit.html.
    #'pokemon': pokemon: el valor es el objeto pokemon recuperado de la base de datos mediante la función get_object_or_404(). Este objeto se utiliza para mostrar el nombre del pokemon en la plantilla HTML edit.html en el título de la página o en alguna otra sección de la plantilla.
    return render(request, 'edit.html', context)

def delete(request, pk):
    pokemon = get_object_or_404(Pokemon, pk=pk) #  Se obtiene el objeto Pokemon correspondiente al id proporcionado. Si no existe un objeto con ese id, se lanza una excepción Http404.
    if request.method == 'POST': #verifica si el método de solicitud HTTP es POST.
        pokemon.delete() #  el método de solicitud es POST, se elimina el registro de la base de datos.
        return redirect('index') # Después de eliminar el registro, se redirige al usuario a la página principal.
    context = {'pokemon': pokemon} #Se crea un diccionario llamado context que contiene la información del objeto Pokemon a eliminar.
    return render(request, 'delete.html', context) #  Si el método de solicitud no es POST, se renderiza el archivo delete.html con la información del objeto Pokemon a eliminar.

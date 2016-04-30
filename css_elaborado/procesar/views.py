from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from models import Contenido, Css
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def meter(request):
    if request.method == 'POST':
        css = request.POST.get('css')
        try:
            encontrada = Css.objects.get(recurso="style.css")
            encontrada.css = css
            encontrada.save()
        except Css.DoesNotExist:
            pag = Css(recurso="style.css",css=css)
            pag.save()
        return HttpResponse("<p>Ya dispones de este css</p>")
    return HttpResponse("<p>Realiza un post sobre esta direccion para add css</p>")

@csrf_exempt
def servir(request):
    try:
        encontrada = Css.objects.get(recurso="style.css")
    except Css.DoesNotExist:
        respuesta = "<p>Page.DoesNotExist</p>"
        return HttpResponse(respuesta)
    template = get_template("style.css")
    argumentos = {'color':encontrada.css}
    return HttpResponse(template.render(Context(argumentos)),content_type="text/css")
    return HttpResponse(encontrada.css,content_type="text/css")

def mostrar (request, key):
    try:
        valor = Contenido.objects.get(id=key)
        respuesta = "Name: " + valor.recurso +"</br>"
        respuesta += "Page: " + valor.contenido +"</br>"
    except Contenido.DoesNotExist:
        respuesta = "Esta clave no existe"
    template = get_template("servir.html")
    argumentos = {'usuario':respuesta,'contenido': respuesta}
    return HttpResponse(template.render(Context(argumentos)))

@csrf_exempt
def contenido(request):
    if request.method == "POST":
        recurso = request.POST.get('recurso')
        contenido = request.POST.get('contenido')
        elemento = Contenido(recurso=recurso,contenido=contenido)
        elemento.save()
    listado = Contenido.objects.all()
    respuesta = "<ol>"
    for elemento in listado:
        respuesta += '<li><a href ="'"annotated/"+ str(elemento.id) + '">'
        respuesta += str(elemento.recurso) + '</a>'
    respuesta += "</ol>"

    template = get_template("pag.html")
    argumentos = {'contenido': respuesta}
    return HttpResponse(template.render(Context(argumentos)))
def notFound(request):
    return HttpResponse("Not Found: Argumentos invalidos")

# Django Cheatsheet

## Project management
Start een nieuw project
django-admin startproject hallowereld
er wordt een directory "hallowereld" gemaakt, met daarin manage.py en een directory hallowereld
tevens is een database aangemaakt: db.sqlite3

Start een nieuwe app in een project:
py manage.py startapp hello (in de directory van het project)
Aan de directories wordt toegevoegd diectoy "hello"
Ga dan naar settings.
py (installed_apps) om de nieuwe app ook aan het project toe te voegen

In de directory hello zit een bestand views.py edit dat bestand met de volgende functie:

def index(request):
	return HttpResponse("Hello World!)

HttpResponse is een Django functie die geïmporteerd moet worden:
from django.http import HttpResponse

Maak vervolgens een urls.py file in de hello directory
from django.urls import path

urlpatterns = [path("",views.index, name="index")]

## Django Templates
In een Django (HTML) template kun je variabelen opnemen:
{{ name }}

Logic: 
{%  if newyear %}
`<h1>` YES \`</h1>`
{% else %}
`<h1>` NO \`</h1>`
{% endif %}   //Django requires endif
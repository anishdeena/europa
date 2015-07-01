from django.http import HttpResponse
from core.testneo4j import Person

def index(request):
    pobj = Person()
    person = pobj.createPerson("Anish", "Anish Deenadayalan", "Enterpreneur", "www.anishdeena.com", "http://wikipedia.org/anish")
    return HttpResponse("Hello, world. You're at the index." + person.properties["name"])

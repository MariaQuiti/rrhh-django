from django.shortcuts import render
# from .forms import RecursosForm
from .models import Person
from django.http import HttpResponseRedirect

def v_list(request):

    
    consulta_nombre = Person.objects.all().order_by('firstname')
    filtro_name = request.GET.get("firstname", False)

    if filtro_name:
        consulta_nombre = consulta_nombre.filter(firstname__istartswith = filtro_name)

    p20 = consulta_nombre[:20]
    context = {
        'personas':p20,
        'f_firstname': filtro_name,
    }
    return render(request, 'list.html', context)


def v_create(request):
    context = {}
    return render(request, 'create.html', context)

def v_update(request):
    context = {}
    return render(request, 'update.html', context)

def v_delete(request):
    context = {}
    return render(request, 'delete.html', context)

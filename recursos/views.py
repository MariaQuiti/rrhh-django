from django.shortcuts import render
from .forms import PersonForm
from .models import Person
from django.http import HttpResponseRedirect

def validate_date(text_date):
    from datetime import datetime
    try:
        return datetime.strptime(text_date, "%Y-%m-%d")
    except:
        return False

def v_list(request):

    
    consulta = Person.objects.all().order_by('firstname')
    filtro_name = request.GET.get("firstname", False)

    if filtro_name:
        consulta = consulta.filter(firstname__istartswith = filtro_name)

    


    
    startdate = validate_date(request.GET.get('startdate', False))
    enddate = validate_date(request.GET.get('enddate', False))
    
    if startdate and enddate:
        consulta = consulta.filter(modifieddate__range = (startdate, enddate))
        


    p20 = consulta[:20]

    context = {
        'personas':p20,
        'f_firstname': filtro_name if filtro_name else '',
        'ordenes': consulta,
    }
    return render(request, 'list.html', context)




def v_create(request):
    context = {}
    return render(request, 'create.html', context)

def v_update(request):

    per = Person.objects.get(id = businessentityid)

    if request.method == 'POST':
        datos = request.POST.copy()
        formeditar = PersonForm(datos, instance = per)
        if formeditar.is_valid():
            formeditar.save()
        return HttpResponseRedirect("/")
    else:
        context = {
            'formedicion': PersonForm(instance = per)
        }
        return render(request, 'update.html', context)

    # context = {}
    # return render(request, 'update.html', context)

def v_delete(request):
    context = {}
    return render(request, 'delete.html', context)

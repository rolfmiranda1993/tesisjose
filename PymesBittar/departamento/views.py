from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from .models import departamento

# Create your views here.
def departamento_views(request):
    #Departamentos = departamento.objects.all()
   # context = {
    #    'rubros': Rubros,
   # }
    return render(request, 'departamento.html')
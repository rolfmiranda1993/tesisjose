from django.shortcuts import render, redirect
from .models import tarea
from .forms import AddTareaForm, EditTareaForm
from django.contrib import messages

# Create your views here.
def tarea_views(request):
    Tarea = tarea.objects.all()
    form_personal = AddTareaForm()
    form_editar = EditTareaForm()
    context = {
        'tareas': Tarea,
        'form_personal' : form_personal,
        'form_editar' : form_editar
    }
    return render(request, 'tarea.html',context)

def add_tarea_views(request):
    if request.POST:
        form = AddTareaForm(request.POST,request.FILES)
        if form.is_valid:
            try:
                form.save()
            except:
                messages(request,"Error al guardar la tarea")
                return redirect('tarea')
    return redirect('tarea')

def edit_tarea_views(request):
    if request.POST:
        Tarea = tarea.objects.get(pk=request.POST.get('id_editar_personal'))
        form =EditTareaForm(request.POST,request.FILES,instance=Tarea)
        if form.is_valid:
            form.save()
    return redirect('tarea')

def delete_tarea_views(request):
    if request.POST:
        Tarea = tarea.objects.get(pk=request.POST.get('id_eliminar_personal'))
        Tarea.delete()
    return redirect('tarea')
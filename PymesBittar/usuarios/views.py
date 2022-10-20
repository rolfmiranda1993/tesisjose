from django.shortcuts import redirect, render
from usuarios.models import usuario
from .forms import AddUsuarioForm, EditUsuarioForm
from django.contrib import messages

# Create your views here.

def usuarios_views(request):
    usuarios = usuario.objects.all()
    form_personal = AddUsuarioForm()
    form_editar = EditUsuarioForm()
    context = {
        'usuarios' : usuarios,
        'form_personal': form_personal,
        'form_editar': form_editar
    }
    return render(request, 'usuarios.html', context)
    
def add_usuarios_views(request):
    #print("Guardar Usuario")
    if request.POST:
        form = AddUsuarioForm(request.POST, request.FILES)
        if form.is_valid:
            try:
                form.save()
            except:
                messages(request, "Error al guardar el Usuario")
                return redirect('Usuarios')
    return redirect('Usuarios')

def edit_usuarios_views(request):
    if request.POST:
        usuarios = usuario.objects.get(pk=request.POST.get('id_personal_editar'))
        form = EditUsuarioForm(request.POST,request.FILES, instance=usuarios)
        if form.is_valid:
            form.save()
    return redirect('Usuarios')

def delete_usuarios_views(request):
    if request.POST:
        usuarios = usuario.objects.get(pk=request.POST.get('id_personal_eliminar'))
        usuarios.delete()
    return redirect('Usuarios')
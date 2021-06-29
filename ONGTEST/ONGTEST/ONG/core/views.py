from django.shortcuts import render
from .models import Proveedor
from .forms import ProveedorFormulario

# Create your views here.

def inicio (request):
    return render(request,'core/index.html')

def nosotros (request):
    return render(request,'core/nosotros.html')

def perros (request):
    return render(request,'core/perros.html')

def gatos (request):
    return render(request,'core/gatos.html')

def formulario (request):
    return render(request,'core/formulario.html')

def test (request):
    return render(request,'core/test.html')

def proveedor (request):
    proveedor= Proveedor.objects.all()
    return render(request, 'core/proveedor.html', {'proveedor': proveedor})

def nuevo_proveedor(request):
    datos = {
        'form': ProveedorFormulario()
    }
    if request.method == 'POST':
        nuevoProveedor = ProveedorFormulario(data=request.POST)
        if nuevoProveedor.is_valid():
           nuevoProveedor.save()
           datos['mensaje'] = "Guardado"
        else:
            datos["form"] = ProveedorFormulario
    
    return render(request, 'core/test.html', datos)




#def nuevo_proveedor(request):
#    datos = {
#        'form': ProveedorFormulario()
#    }
#    if request.method == 'POST':
#        nuevoProveedor = ProveedorFormulario(request.POST)
#        if nuevoProveedor.is_valid():
#           nuevoProveedor.save()
#           datos['mensaje'] = "guardado"
    
#    return render(request, 'core/test.html', datos)

#def nuevo_proveedor(request):
 #   proveedor = Proveedor()

  #  if request.method == 'POST':
  #      nuevoProveedor = ProveedorFormulario(request.POST, instance=proveedor)
  #      nuevoProveedor.save() 
  #      proveedor= Proveedor.objects.all()
  #      return render(request, 'core/proveedor.html', {'proveedor':proveedor})
  #  else:
  #      formulario = ProveedorFormulario()
  #      return render(request, 'core/test.html', {'formulario': formulario})


       

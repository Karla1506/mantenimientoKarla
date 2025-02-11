from django.shortcuts import redirect, render, get_object_or_404
from.models import Estructura
from.models import Encargado
from.models import PlanMantenimiento
from.models import Trabajo

# Create your views here.
from django.contrib import messages


def inicio(request):
    return render(request,'inicio.html')

from django.shortcuts import render, redirect


#--------------------------------------------------------------Estructuras----------------------------------------------------------


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Estructura

def nuevaEstructura(request):
    estados_choices = Estructura.ESTADO_CHOICES
    return render(request, 'nuevaEstructura.html', {'estados_choices': estados_choices})

def guardarEstructura(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        tipo = request.POST.get('tipo')
        ubicacion = request.POST.get('ubicacion')
        fecha_construccion = request.POST.get('fecha_construccion')
        estado = request.POST.get('estado')
        descripcion = request.POST.get('descripcion')
        imagen = request.FILES.get('imagen')

        estructura = Estructura(
            nombre=nombre,
            tipo=tipo,
            ubicacion=ubicacion,
            fecha_construccion=fecha_construccion,
            estado=estado,
            descripcion=descripcion,
            imagen=imagen
        )
        estructura.save()
        messages.success(request, "Estructura registrada exitosamente.")
        return redirect('listadoEstructura')
    return render(request, 'nuevaEstructura.html')

def listadoEstructura(request):
    nombre = request.GET.get('nombre', '')
    estructuras = Estructura.objects.all()
    if nombre:
        estructuras = estructuras.filter(nombre__icontains=nombre)
    return render(request, 'listadoEstructura.html', {'estructuras': estructuras})

def eliminarEstructura(request, estructura_id):
    estructura_eliminar = get_object_or_404(Estructura, id=estructura_id)
    estructura_eliminar.delete()
    messages.success(request, "Estructura eliminada exitosamente.")
    return redirect('listadoEstructura')

def editarEstructura(request, estructura_id):
    estructura = get_object_or_404(Estructura, id=estructura_id)
    
    if request.method == 'POST':
        # Obtención de los datos del formulario
        estructura.nombre = request.POST.get('nombre')
        estructura.tipo = request.POST.get('tipo')
        estructura.ubicacion = request.POST.get('ubicacion')
        estructura.fecha_construccion = request.POST.get('fecha_construccion')
        estructura.estado = request.POST.get('estado')
        estructura.descripcion = request.POST.get('descripcion')

        # Si se sube una nueva imagen
        if request.FILES.get('imagen'):
            estructura.imagen = request.FILES.get('imagen')

        # Guardar los cambios en el registro
        estructura.save()

        # Mensaje de éxito
        messages.success(request, "Estructura actualizada con éxito.")
        
        # Redirigir al listado de estructuras
        return redirect('listadoEstructura')

    # Si el método no es POST, renderizar el formulario de edición
    return render(request, 'editarEstructura.html', {
        'estructura': estructura,
        'estados_choices': Estructura.ESTADO_CHOICES,  # Pasando los posibles estados de la estructura
    })

def procesarEdicionEstructura(request, id):
    if request.method == 'POST':
        estructura = get_object_or_404(Estructura, id=id)
        estructura.nombre = request.POST.get('nombre')
        estructura.tipo = request.POST.get('tipo')
        estructura.ubicacion = request.POST.get('ubicacion')
        estructura.fecha_construccion = request.POST.get('fecha_construccion')
        estructura.estado = request.POST.get('estado')
        estructura.descripcion = request.POST.get('descripcion')

        if request.FILES.get('imagen'):
            estructura.imagen = request.FILES.get('imagen')
        
        estructura.save()
        messages.success(request, "Estructura actualizada con éxito.")
        return redirect('listadoEstructura')
    return redirect('listadoEstructura')



#--------------------------------------------ENCARGADO--------------------------------------------------------------------------




# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Encargado

def nuevoEncargado(request):
    return render(request, 'nuevoEncargado.html')

def guardarEncargado(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        cargo = request.POST.get('cargo')
        telefono = request.POST.get('telefono')
        email = request.POST.get('email')
        especialidad = request.POST.get('especialidad')
        estado = request.POST.get('estado')  # Este es el valor del checkbox
        foto = request.FILES.get('foto')

        # Si el checkbox 'estado' no fue marcado, se asigna 'False' por defecto
        if estado == 'on':
            estado = True
        else:
            estado = False

        # Validación de campos
        if not nombre or not cargo or not telefono or not email or not especialidad:
            messages.error(request, "Todos los campos son obligatorios.")
            return redirect('nuevoEncargado')

        # Guardar encargado
        encargado = Encargado(
            nombre=nombre,
            cargo=cargo,
            telefono=telefono,
            email=email,
            especialidad=especialidad,
            estado=estado,  # Usar el valor del checkbox
            foto=foto
        )
        encargado.save()
        messages.success(request, "Encargado registrado exitosamente.")
        return redirect('listadoEncargado')
    return render(request, 'nuevoEncargado.html')


def listadoEncargado(request):
    nombre = request.GET.get('nombre', '')
    encargados = Encargado.objects.all()
    if nombre:
        encargados = encargados.filter(nombre__icontains=nombre)
    return render(request, 'listadoEncargado.html', {'encargados': encargados})

def eliminarEncargado(request, encargado_id):
    encargado_eliminar = get_object_or_404(Encargado, id=encargado_id)
    encargado_eliminar.delete()
    messages.success(request, "Encargado eliminado exitosamente.")
    return redirect('listadoEncargado')

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Encargado

def editarEncargado(request, encargado_id):
    # Verifica si el encargado existe en la base de datos
    encargado = get_object_or_404(Encargado, id=encargado_id)
    print(f"Editando encargado: {encargado.nombre}")  # Depuración

    if request.method == 'POST':
        encargado.nombre = request.POST.get('nombre', encargado.nombre)
        encargado.cargo = request.POST.get('cargo', encargado.cargo)
        encargado.telefono = request.POST.get('telefono', encargado.telefono)
        encargado.email = request.POST.get('email', encargado.email)
        encargado.especialidad = request.POST.get('especialidad', encargado.especialidad)
        encargado.estado = request.POST.get('estado') == 'on'  # Verifica si el checkbox está activado

        if request.FILES.get('foto'):
            encargado.foto = request.FILES.get('foto')

        encargado.save()
        messages.success(request, "Encargado actualizado con éxito.")
        return redirect('listadoEncargado')

    return render(request, 'editarEncargado.html', {
        'encargado': encargado,  # Envia el objeto a la plantilla
    })



from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Encargado
from django.core.files.storage import FileSystemStorage

def procesarEdicionEncargado(request, id):
    encargado = get_object_or_404(Encargado, id=id)

    if request.method == 'POST':
        estado = request.POST.get('estado') == 'on'  # Manejo del checkbox correctamente
        
        encargado.nombre = request.POST.get('nombre')
        encargado.cargo = request.POST.get('cargo')
        encargado.telefono = request.POST.get('telefono')
        encargado.email = request.POST.get('email')
        encargado.especialidad = request.POST.get('especialidad')
        encargado.estado = estado  # Guardar el estado convertido
        
        # Manejo de la foto
        if request.FILES.get('foto'):
            foto = request.FILES['foto']
            fs = FileSystemStorage()
            filename = fs.save(foto.name, foto)  # Guardar el archivo
            encargado.foto = fs.url(filename)  # Asignar la URL al campo foto
        
        encargado.save()
        messages.success(request, "Encargado actualizado correctamente.")
        return redirect('listadoEncargado')

    return render(request, 'editarEncargado.html', {'encargado': encargado})



#-----------------------------------------------------------------MANTENIMIENTO-----------------------------------------------------

from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import PlanMantenimiento, Estructura

def nuevoMantenimiento(request):
    estructuras = Estructura.objects.all()  # Obtener todas las estructuras para el formulario
    return render(request, 'nuevoMantenimiento.html', {'estructuras': estructuras})

def guardarPlanMantenimiento(request):
    if request.method == 'POST':
        estructura_id = request.POST.get('estructura')
        tipo = request.POST.get('tipo')
        fecha_inicio = request.POST.get('fecha_inicio')
        fecha_fin = request.POST.get('fecha_fin', None)
        estado = request.POST.get('estado')
        descripcion = request.POST.get('descripcion')
        documento = request.FILES.get('documento')

        if not estructura_id or not tipo or not fecha_inicio or not estado:
            messages.error(request, "Todos los campos son obligatorios.")
            return redirect('nuevoMantenimiento')

        plan_mantenimiento = PlanMantenimiento(
            estructura_id=estructura_id,
            tipo=tipo,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin if fecha_fin else None,
            estado=estado,
            descripcion=descripcion,
            documento=documento
        )
        plan_mantenimiento.save()
        messages.success(request, "Plan de mantenimiento registrado exitosamente.")
        return redirect('listadoMantenimiento')

    return render(request, 'nuevoMantenimiento.html')

def listadoMantenimiento(request):
    mantenimientos = PlanMantenimiento.objects.all()
    return render(request, 'listadoMantenimiento.html', {'mantenimientos': mantenimientos})


def eliminarMantenimiento(request, pk):
    plan = get_object_or_404(PlanMantenimiento, pk=pk)
    plan.delete()
    return redirect('listadoMantenimiento')

def editarMantenimiento(request, mantenimiento_id):
    mantenimiento = get_object_or_404(PlanMantenimiento, id=mantenimiento_id)
    estructuras = Estructura.objects.all()  # Obtener las estructuras para el select

    if request.method == 'POST':
        mantenimiento.estructura_id = request.POST.get('estructura')
        mantenimiento.tipo = request.POST.get('tipo')
        mantenimiento.fecha_inicio = request.POST.get('fecha_inicio')
        mantenimiento.fecha_fin = request.POST.get('fecha_fin', None)
        mantenimiento.estado = request.POST.get('estado')
        mantenimiento.descripcion = request.POST.get('descripcion')
        if request.FILES.get('documento'):
            mantenimiento.documento = request.FILES.get('documento')

        mantenimiento.save()
        messages.success(request, "Plan de mantenimiento actualizado con éxito.")
        return redirect('listadoMantenimiento')

    return render(request, 'editarMantenimiento.html', {
        'mantenimiento': mantenimiento,
        'estructuras': estructuras
    })
    
    
def procesarEdicionMantenimiento(request, mantenimiento_id):
    mantenimiento = get_object_or_404(PlanMantenimiento, id=mantenimiento_id)

    if request.method == 'POST':
        mantenimiento.estructura_id = request.POST.get('estructura')
        mantenimiento.tipo = request.POST.get('tipo')
        mantenimiento.fecha_inicio = request.POST.get('fecha_inicio')  # Capturamos la fecha de inicio
        mantenimiento.fecha_fin = request.POST.get('fecha_fin', None)  # Capturamos la fecha de fin, puede ser None
        mantenimiento.estado = request.POST.get('estado')
        mantenimiento.descripcion = request.POST.get('descripcion')
        
        if request.FILES.get('documento'):  # Si hay un nuevo archivo subido
            mantenimiento.documento = request.FILES.get('documento')

        mantenimiento.save()  # Guardamos los cambios
        messages.success(request, "Plan de mantenimiento actualizado correctamente.")
        return redirect('listadoMantenimiento')  # Redirigimos a la lista de mantenimientos

    # Si no es un POST, pasamos los datos a la plantilla
    return render(request, 'editarMantenimiento.html', {'mantenimiento': mantenimiento})


#-----------------------------------------------------------------TRABAJOS----------------------------------------------------------


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import PlanMantenimiento, Encargado, Trabajo

def nuevoTrabajo(request):
    planes = PlanMantenimiento.objects.all()
    encargados = Encargado.objects.all()
    
    print("Planes de Mantenimiento:", planes)  # Verificar que hay datos
    
    context = {
        'planes': planes,
        'encargados': encargados,
        'datos_formulario': {},
    }
    return render(request, 'nuevoTrabajo.html', context)


def listadoTrabajo(request):
    trabajos = Trabajo.objects.all()  # Debe ser el modelo correcto
    return render(request, 'listadoTrabajo.html', {'trabajos': trabajos})


def guardarTrabajo(request):
    if request.method == "POST":
        plan_id = request.POST.get("plan")
        encargado_id = request.POST.get("encargado")
        descripcion = request.POST.get("descripcion")
        fecha_inicio = request.POST.get("fecha_inicio")
        fecha_fin = request.POST.get("fecha_fin") if request.POST.get("fecha_fin") else None
        costo = request.POST.get("costo")
        estado = request.POST.get("estado")
        evidencia = request.FILES.get("evidencia")

        try:
            plan = PlanMantenimiento.objects.get(id=plan_id)
            encargado = Encargado.objects.get(id=encargado_id) if encargado_id else None

            trabajo = Trabajo.objects.create(
                plan=plan,
                encargado=encargado,
                descripcion=descripcion,
                fecha_inicio=fecha_inicio,
                fecha_fin=fecha_fin,
                costo=costo,
                estado=estado,
                evidencia=evidencia
            )

            messages.success(request, "Trabajo de mantenimiento guardado exitosamente.")
            return redirect("listadoTrabajo")

        except PlanMantenimiento.DoesNotExist:
            messages.error(request, "El plan de mantenimiento seleccionado no existe.")
        except Encargado.DoesNotExist:
            messages.error(request, "El encargado seleccionado no existe.")
        except Exception as e:
            messages.error(request, f"Error al guardar el trabajo: {str(e)}")

    return redirect("listadoTrabajo")

def eliminarTrabajo(request, pk):
    trabajo = get_object_or_404(Trabajo, pk=pk)
    try:
        trabajo.delete()
        messages.success(request, "Trabajo eliminado correctamente.")
    except Exception as e:
        messages.error(request, f"Error al eliminar el trabajo: {str(e)}")
    return redirect('listadoTrabajo')


def editarTrabajo(request, trabajo_id):
    trabajo = get_object_or_404(Trabajo, id=trabajo_id)
    encargados = Encargado.objects.all()
    planes = PlanMantenimiento.objects.all()

    if request.method == 'POST':
        try:
            # Actualizando los datos del trabajo con los datos del formulario
            trabajo.encargado_id = int(request.POST.get('encargado', trabajo.encargado_id))
            trabajo.plan_id = int(request.POST.get('plan', trabajo.plan_id))
            trabajo.descripcion = request.POST.get('descripcion', trabajo.descripcion)
            trabajo.fecha_inicio = request.POST.get('fecha_inicio', trabajo.fecha_inicio)
            trabajo.fecha_fin = request.POST.get('fecha_fin', trabajo.fecha_fin)
            
            # Asegurándose de que 'costo' sea un número válido
            costo = request.POST.get('costo', None)
            if costo:
                trabajo.costo = float(costo)  # Convertir a float si el campo 'costo' no está vacío
            else:
                trabajo.costo = 0.0  # O un valor predeterminado si no se proporciona

            trabajo.estado = request.POST.get('estado', trabajo.estado)

            # Verificando si hay un archivo para la evidencia
            if request.FILES.get('evidencia'):
                trabajo.evidencia = request.FILES.get('evidencia')

            trabajo.save()
            messages.success(request, "Trabajo actualizado con éxito.")
            return redirect('listadoTrabajo')  # Redirige a la lista de trabajos

        except ValueError:
            messages.error(request, "Datos inválidos en el formulario. Asegúrese de que los campos sean correctos.")

    # Renderiza el formulario para editar el trabajo
    return render(request, 'editarTrabajo.html', {
        'trabajo': trabajo,
        'encargados': encargados,
        'planes': planes,  # Asegura que los planes estén disponibles en la plantilla
    })

    
    
def procesarEdicionTrabajo(request, trabajo_id):
    trabajo = get_object_or_404(Trabajo, id=trabajo_id)
    encargados = Encargado.objects.all()
    planes = PlanMantenimiento.objects.all()

    if request.method == 'POST':
        trabajo.encargado_id = request.POST.get('encargado')
        trabajo.plan_id = request.POST.get('plan')  # Se agrega el plan
        trabajo.descripcion = request.POST.get('descripcion')
        trabajo.fecha_inicio = request.POST.get('fecha_inicio')
        trabajo.fecha_fin = request.POST.get('fecha_fin', None)
        trabajo.costo = request.POST.get('costo')
        trabajo.estado = request.POST.get('estado')

        if request.FILES.get('evidencia'):
            trabajo.evidencia = request.FILES.get('evidencia')

        trabajo.save()
        messages.success(request, "Trabajo de mantenimiento actualizado con éxito.")
        return redirect('listadoTrabajo')

    return render(request, 'editarTrabajo.html', {
        'trabajo': trabajo,
        'encargados': encargados,
        'planes': planes  # Asegurar que los planes estén en la plantilla
    })

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio),



#------------------------------------------------------ESTRUCTURAS---------------------------------------------------------------

path('nuevaEstructura/', views.nuevaEstructura, name='nuevaEstructura'),
    path('guardar/', views.guardarEstructura, name='guardarEstructura'),
    path('listadoEstructura/', views.listadoEstructura, name='listadoEstructura'),
    path('eliminar/<int:estructura_id>/', views.eliminarEstructura, name='eliminarEstructura'),
     path('editarEstructura/<int:estructura_id>/', views.editarEstructura, name='editarEstructura'),
    path('procesar-edicion/<int:id>/', views.procesarEdicionEstructura, name='procesarEdicionEstructura'),
    
    
#----------------------------------------------------------ENCARGADOS--------------------------------------------------------------


    path('nuevoEncargado/', views.nuevoEncargado, name='nuevoEncargado'),
    path('guardarEncargado/', views.guardarEncargado, name='guardarEncargado'),
    path('listadoEncargado/', views.listadoEncargado, name='listadoEncargado'),
    path('eliminarEncargado/<int:encargado_id>/', views.eliminarEncargado, name='eliminarEncargado'),
    path('editarEncargado/<int:encargado_id>/', views.editarEncargado, name='editarEncargado'),
    path('procesarEdicionEncargado/<int:id>/', views.procesarEdicionEncargado, name='procesarEdicionEncargado'),
    
    
    
#---------------------------------------------------MANTENIMIENTO-------------------------------------------------------------------

path('nuevoMantenimiento/', views.nuevoMantenimiento, name='nuevoMantenimiento'),
    path('guardarPlanMantenimiento/', views.guardarPlanMantenimiento, name='guardarPlanMantenimiento'),
    path('listadoMantenimiento/', views.listadoMantenimiento, name='listadoMantenimiento'),
    path('eliminarMantenimiento/<int:pk>/', views.eliminarMantenimiento, name='eliminarMantenimiento'),
    path('editarMantenimiento/<int:mantenimiento_id>/', views.editarMantenimiento, name='editarMantenimiento'),
    path('procesarEdicionMantenimiento/<int:mantenimiento_id>/', views.procesarEdicionMantenimiento, name='procesarEdicionMantenimiento'),


#-------------------------------------------------------------------TRABAJO-----------------------------------------------------------

path('nuevoTrabajo/', views.nuevoTrabajo, name='nuevoTrabajo'),
    path('listadoTrabajo/', views.listadoTrabajo, name='listadoTrabajo'),
    path('eliminarTrabajo/<int:pk>/', views.eliminarTrabajo, name='eliminarTrabajo'),
    path('editarTrabajo/<int:trabajo_id>/', views.editarTrabajo, name='editarTrabajo'),
    path('guardarTrabajo/', views.guardarTrabajo, name='guardarTrabajo'),
    path('editarTrabajo/<int:trabajo_id>/', views.editarTrabajo, name='editarTrabajo'),
    path('procesarEdicionTrabajo/<int:trabajo_id>/', views.procesarEdicionTrabajo, name='procesarEdicionTrabajo'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
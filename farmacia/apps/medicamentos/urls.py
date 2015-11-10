from django.conf.urls import patterns, url
from .views import ListaMedicamentos, DetalleView,ActualizarView, CreateMedicamentos, EliminarView,CargaAtenciones_ant

urlpatterns = patterns('',

	url(r'^medicamentos/$', ListaMedicamentos.as_view(), name = 'lista_medicamentos'),
	url(r'^medicamentos/detalle/(?P<pk>\d+)/$', DetalleView.as_view(), name ='detalle_medicamentos'),
	url(r'^medicamentos/actualizar/(?P<pk>\d+)/$', ActualizarView.as_view(), name ="actualizar_medicamentos"),
	url(r'^medicamentos/agregar$', CreateMedicamentos.as_view(), name='create_medicamentos'),
	url(r'^medicamentos/eliminar/(?P<pk>\d+)/$', EliminarView.as_view(), name="eliminar_medicamentos"), 
	url(r'^expatenciones/$', 'apps.medicamentos.views.CargaAtenciones_ant',name='xds'),
	)
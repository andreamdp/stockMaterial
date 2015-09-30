from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from aplicacion.forms import *
from aplicacion.models import *
from django import template
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from reportlab.lib.colors import navy, yellow, red, black, blue, purple, green, darkgreen, lightblue
from django.http import HttpResponse
register = template.Library()  


def residente_list(request,residenciaaut_id,template_name='aplicacion/residente/list.html' ):
    residenciaActual=ResidenciaAut.objects.filter(id=residenciaaut_id)
    residentes_list = Residente.active.filter(residencia_id=residenciaaut_id).order_by('tipoR')
  #  paginator = Paginator(residentes_list,  6)
  #  page = request.GET.get('page')
  #  try:
  #      residentes = paginator.page(page)
  #  except PageNotAnInteger:
  #      residentes = paginator.page(1)
  #  except EmptyPage:
  #      residentes = paginator.page(paginator.num_pages)
    return render_to_response(template_name, {
        'residentes': residentes_list,
        'idR:': Residente.residencia,
        'residencia': ResidenciaAut.objects.filter(id=residenciaaut_id)
      #  'paginator': paginator,
      #  'page': page,
    })
def residente_edit(request,residenciaaut_id, residente_id):
    residente = get_object_or_404(Residente, pk=residente_id)
    form = ResidenteForm1(request.POST or None, instance=residente)
    if form.is_valid():
        residente = form.save()
        return redirect('/'+residenciaaut_id+'/lista/')

    return render_to_response('aplicacion/residente/edit.html',
                              {'form': form,
                               'residente_id': residente_id},
                              context_instance=RequestContext(request))    
def residente_delete(request,residenciaaut_id, residente_id):
    residente = get_object_or_404(Residente, pk=residente_id)
    residente.delete()
    return redirect('/aplicacion/residenciaaut/'+residenciaaut_id+'/lista/')

@csrf_protect
@register.inclusion_tag('aplicacion/residente/add.html', takes_context=True)
def residente1_add(request, residenciaaut_id,form_class=ResidenteForm1, template_name='aplicacion/residente/add.html'):
    if request.POST:
        form = form_class(request.POST)
        if form.is_valid():
            residente = form.save()
            return redirect('residente_list',residenciaaut_id)
    else:
       form = ResidenteForm1(initial={'residencia': residenciaaut_id})  
    return render_to_response(template_name,{'form':form,'idResidencia':residenciaaut_id},context_instance=RequestContext(request))

@csrf_protect
#@register.inclusion_tag('aplicacion/residente/add.html', takes_context=True)
def residente2_add(request, residenciaaut_id,form_class=ResidenteForm2, template_name='aplicacion/residente/add.html'):
    if request.POST:
        form = form_class(request.POST)
        if form.is_valid():
            residente = form.save()
            return redirect('residente_list',residenciaaut_id)
    else:
       form = ResidenteForm2(initial={'residencia': residenciaaut_id})
    return render_to_response(template_name,{'form':form,'idResidencia':residenciaaut_id},context_instance=RequestContext(request))   
@csrf_protect

def residente3_add(request, residenciaaut_id,form_class=ResidenteForm3, template_name='aplicacion/residente/add.html'):
    if request.POST:
        form = form_class(request.POST)
        if form.is_valid():
            residente = form.save()
            return redirect('residente_list',residenciaaut_id)
    else:
       form = ResidenteForm3(initial={'residencia': residenciaaut_id})
    return render_to_response(template_name,{'form':form,'idResidencia':residenciaaut_id},context_instance=RequestContext(request))
@csrf_protect

def residente4_add(request, residenciaaut_id,form_class=ResidenteForm4, template_name='aplicacion/residente/add.html'):
    if request.POST:
        form = form_class(request.POST)
        if form.is_valid():
            residente = form.save()
            return redirect('residente_list',residenciaaut_id)
    else:
       form = ResidenteForm4(initial={'residencia': residenciaaut_id})
    return render_to_response(template_name,{'form':form,'idResidencia':residenciaaut_id},context_instance=RequestContext(request))

@csrf_protect
def jefeResidente_add(request, residenciaaut_id,form_class=JefeResidenteForm, template_name='aplicacion/residente/add.html'):
    if request.POST:
        form = form_class(request.POST)
        if form.is_valid():
            residente = form.save()
            return redirect('residente_list',residenciaaut_id)
    else:
       form = JefeResidenteForm(initial={'residencia': residenciaaut_id})
    return render_to_response(template_name,{'form':form,'idResidencia':residenciaaut_id},context_instance=RequestContext(request))   

#---------------------------------Listado de Instituciones ----------------------------------------------
class R_Intitucion(UsersReport):
    title = 'Listado de Instituciones'
    page_size = landscape(legal)
    class band_page_header(ReportBand):
        height = 3*cm
        elements = [
            SystemField(expression='%(report_title)s', top=0.1*cm, left=0, width=BAND_WIDTH,
                style={'fontSize': 20, 'alignment': TA_CENTER,  'textColor': navy}),
            Label(text="Nombre", top=2*cm, left=0, style={ 'fontSize': 10, 'textColor': darkgreen, 'fontName': 'Helvetica-Bold'}),
            Label(text="Localidad", top=2*cm, left=6*cm, style={ 'fontSize': 10, 'textColor': darkgreen, 'fontName': 'Helvetica-Bold'}),
            Label(text="Director", top=2*cm, left=9*cm, style={ 'fontSize': 10, 'textColor': darkgreen, 'fontName': 'Helvetica-Bold'}),
            Label(text="Secretaria ", top=2*cm, left=15*cm, style={ 'fontSize': 10, 'textColor': darkgreen, 'fontName': 'Helvetica-Bold'}),
            Label(text="Telefonos", top=2*cm, left=21.5*cm, style={ 'fontSize': 10, 'textColor': darkgreen, 'fontName': 'Helvetica-Bold'}),
            Label(text="Otros Contactos", top=2*cm, left=28*cm, style={ 'fontSize': 10, 'textColor': darkgreen, 'fontName': 'Helvetica-Bold'}),
                    ]
        borders = {'bottom': Line(stroke_color=red, stroke_width=1)}
    
    class band_detail(DetailBand):
        
        height=3.5*cm
        elements=[
            ObjectValue(attribute_name='nombre', top=0.1*cm, left=0.001, width=5*cm),
            ObjectValue(attribute_name='localidad', top=0.2*cm, left=6*cm, width=8*cm),
            ObjectValue(attribute_name='director', top=0.2*cm, left=9*cm, width=6*cm),
            ObjectValue(attribute_name='secretaria', top=0.2*cm, left=14.7*cm, width=6*cm),
            ObjectValue(attribute_name='telefonos', top=0.2*cm, left=21.5*cm ),
            ObjectValue(attribute_name='OtrosContactos', top=0.2*cm, left=27*cm, width=6*cm),
          
            ]



def Instituciones(request):
    response = HttpResponse(mimetype='application/pdf')
    objects_list = Institucion.objects.all().order_by('nombre') 
    report = R_Intitucion(queryset=objects_list)
    
    report.generate_by(PDFGenerator, filename=response)

    return response


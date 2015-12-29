from django.shortcuts import render, get_object_or_404
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView, FormView
from django.core import serializers
from .forms import SignUpForm
from .forms import AddPisoForm
from django.contrib.auth.models import User
import traceback
import tweepy

import json

from .models import Piso, Imagen

class HomePageView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        context = {
            'page': 'home',
            'some_dynamic_value': 'This text comes from django view!',
        }
        
        return self.render_to_response(context)
    
class GetPisos(TemplateView):
    def get(self, request, *args, **kwargs):
        pisos = serializers.serialize("json", Piso.objects.all())
        return HttpResponse(pisos)

class GetImagenesPiso(TemplateView):
    def get(self, request, *args, **kwargs):
        
        imagenes = serializers.serialize("json", Imagen.objects.filter(id_piso=self.kwargs['piso']))
        return HttpResponse(imagenes)

class GetUsuario(TemplateView):
    def get(self, request, *args, **kwargs):
        usuario = serializers.serialize("json", User.objects.filter(id=self.kwargs['id']))
        return HttpResponse(usuario)

def registroUsuario(request):
    if request.method == 'POST':  # If the form has been submitted...
        form = SignUpForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
 
            # Process the data in form.cleaned_data
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            email = form.cleaned_data["email"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
 
            # At this point, user is a User object that has already been saved
            # to the database. You can continue to change its attributes
            # if you want to change other fields.
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
 
            # Save new user attributes
            user.save()
 
            return HttpResponseRedirect("/")  # Redirect after POST
    else:
        form = SignUpForm()
 
    data = {
        'form': form,
    }
    return render_to_response('registroUsuario.html', data, context_instance=RequestContext(request))

def addPiso(request):
    if request.method == 'POST':  # If the form has been submitted...
        form = AddPisoForm(request.POST,request.FILES)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
 
            #'user', 'titulo', 'opciones_piso', 'tipo', 'lat','lng','descripcion','direccion','fecha_registro','precio'
            
            piso = Piso.objects.create()
            piso.titulo = form.cleaned_data["titulo"]
            #piso.opciones_piso = form.cleaned_data["opciones_piso"]
            piso.tipo = form.cleaned_data["tipo"]
            piso.lng = form.cleaned_data["lng"]
            piso.lat = form.cleaned_data["lat"]
            piso.direccion = form.cleaned_data["direccion"]
            piso.fecha_registro = form.cleaned_data["fecha_registro"]
            piso.descripcion = form.cleaned_data["descripcion"]
            piso.precio = form.cleaned_data["precio"]
            piso.user = request.user
            
            img = Imagen.objects.create()
            if 'image' in request.FILES:
                img.pic = request.FILES['image']
            img.id_piso = piso
            
            piso.save()
            img.save()
            
            try:       
                consumer_key = 'ebUuZ2GerfT50yazZBjwixPav'
                consumer_secret = 'Uwlom8kZ10DowJvvZRjagBBfz78C8Csr6n74fI8iNfyI36Fxf3'
                access_token = '2973546431-xASDOdy1A6se3MJWkiC39fZFZyEqsMVJKCgPLOu'
                access_token_secret = 'yoe1mYaFEfrzkM240uAIaTwYIjPyFJBteUqYC5exs5kkP'
                # OAuth process, using the keys and tokens
                auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
                auth.set_access_token(access_token, access_token_secret)
                # Creation of the actual interface, using authentication
                api = tweepy.API(auth)
                infomsg = '%s | %s (%s)' %(piso.titulo,piso.direccion,piso.precio)
                api.update_status(infomsg)
               
            except:
                tb = traceback.format_exc()
                return HttpResponse(tb)
                
                
                
            
            
            
            
 
            return HttpResponseRedirect("/")  # Redirect after POST
    else:
        form = AddPisoForm()
 
    data = {
        'form': form,
    }
    return render_to_response('addPiso.html', data, context_instance=RequestContext(request))

class HighCharts(TemplateView):
    template_name = 'highchart.html'

    def get(self, request, *args, **kwargs):
        n_pisos = Piso.objects.filter(tipo='PISO').count()
        n_habitaciones = Piso.objects.filter(tipo='HABITACION').count()
        context = {'n_pisos': n_pisos, 'n_habitaciones': n_habitaciones}
        return render(request, 'highchart.html', context)

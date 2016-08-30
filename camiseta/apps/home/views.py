from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render_to_response
from django.shortcuts import render_to_response
from django.template import RequestContext
from camiseta.apps.home.forms import *
from camiseta.apps.home.models import *
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.contrib.auth.models import User


def index_view (request):
	return render_to_response('home/index.html', context_instance = RequestContext(request))




def single_camiseta_view(request,id_prod):
	prod = Camiseta.objects.get(id = id_prod)
	ctx = {'camiseta':prod}
	return render_to_response('home/single_camiseta.html',ctx,context_instance = RequestContext(request))

def single_marca_view(request,id_prod):
	prod = Marca.objects.get(id = id_prod)
	ctx = {'marca':prod}
	return render_to_response('home/single_marca.html',ctx,context_instance = RequestContext(request))

def single_talla_view(request,id_prod):
	prod = Talla.objects.get(id = id_prod)
	ctx = {'talla':prod}
	return render_to_response('home/single_talla.html',ctx,context_instance = RequestContext(request))

def camisetas_view(request, pagina):
	lista_prod = Camiseta.objects.filter() 
	paginator = Paginator(lista_prod, 5)
	try:
		page = int(pagina)
	except :
		page = 1
	try:
		camisetas = paginator.page(page)
	except (EmptyPage,InvalidPage):
		camisetas = paginator.page(paginator.num_pages)
	
	ctx = {'camisetas':camisetas}
	return render_to_response ('home/camisetas.html',ctx, context_instance = RequestContext(request))



def login_view(request):
	mensaje = ""
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	else:
		if request.method == "POST":
			formulario = Login_form(request.POST)
			if formulario.is_valid():
				usu = formulario.cleaned_data['usuario']
				pas = formulario.cleaned_data['clave']
				usuario = authenticate(username = usu,password = pas)
				if usuario is not None and usuario.is_active:
					login(request,usuario)
					return HttpResponseRedirect('/')
				else:
					mensaje = "usuario y/o clave incorrecta"
		formulario = Login_form()
		ctx = {'form':formulario,'mensaje':mensaje}
		return render_to_response('home/login.html',ctx, context_instance = RequestContext(request))

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')

def register_view(request):
	form = RegisterForm()
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			usuario = form.cleaned_data['username']
			email = form.cleaned_data['email']
			password_one = form.cleaned_data['password_one']
			password_two = form.cleaned_data['password_two']
			u = User.objects.create_user(username=usuario,email=email,password=password_one)
			u.save()
			return render_to_response('home/thanks_register.html', context_instance=RequestContext(request))
		else:
			ctx = {'form':form}
			return render_to_response('home/register.html',ctx, context_instance = RequestContext(request))
	ctx = {'form':form}
	return render_to_response('home/register.html',ctx, context_instance = RequestContext(request))



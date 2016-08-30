from camiseta.apps.home.models import *
from django import forms

class add_camiseta_form(forms.ModelForm):
	class Meta:
		model   = Camiseta 

		exclude = {'status',}


class add_marca_form(forms.ModelForm):
	class Meta:
		model   = Marca



class add_modelo_form(forms.ModelForm):
	class Meta:
		model   = Modelo


class add_talla_form(forms.ModelForm):
	class Meta:
		model   = Talla 


class add_material_form(forms.ModelForm):
	class Meta:
		model   = Material


class Login_form(forms.Form):
	usuario = forms.CharField(widget = forms.TextInput())
	clave = forms.CharField(widget = forms.PasswordInput(render_value =False))
	
class RegisterForm(forms.Form):
	username = forms.CharField(label="Nombre de Usuario",widget=forms.TextInput())
	email  = forms.EmailField(label="Correo Electronico",widget=forms.TextInput())
	password_one = forms.CharField(label=" Password",widget=forms.PasswordInput(render_value=False))
	password_two = forms.CharField(label=" Confirmar Password",widget=forms.PasswordInput(render_value=False))

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			u = User.objects.get(username=username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError('Nombre de usuario ya existe')

	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			u = User.objects.get(email=email)
		except User.DoesNotExist:
			return email
		raise forms.ValidationError('Email ya registrado')

	def clean_password_two(self):
		password_one =self.cleaned_data ['password_one']
		password_two =self.cleaned_data ['password_two']
		if password_one == password_two:
			pass
		else:
			raiseforms.ValidationError('Password no coinciden')


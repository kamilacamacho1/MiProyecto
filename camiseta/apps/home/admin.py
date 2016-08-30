from django.contrib import admin
from camiseta.apps.home.models import *

admin.site.register(user_profile)
admin.site.register(Marca)
admin.site.register(Camiseta)
admin.site.register(Modelo)
admin.site.register(Material)
admin.site.register(Talla)

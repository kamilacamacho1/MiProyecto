from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('camiseta.apps.home.views',
		url(r'^$','index_view', name = 'vista_principal'),
		#url(r'^add/camiseta/$','add__camiseta_view', name = 'vista_agregar_camiseta'),
		url(r'^camiseta/(?P<id_prod>.*)$','single_camiseta_view', name = 'vista_single_camiseta'),
		url(r'^marca/(?P<id_prod>.*)$','single_marca_view', name = 'vista_single_marca'),
		url(r'^talla/(?P<id_prod>.*)$','single_talla_view', name = 'vista_single_talla'),
   		
   		
   		#url(r'^camisetas$','camisetas_view', name = 'vista_camisetas'),
		#url(r'^camisetas/page/(?P<pagina>.*)/$', 'camisetas_view', name = 'vista_camisetas'),

		url(r'^login/$','login_view', name ='vista_login'),
		url(r'^logout/$','logout_view', name = 'vista_logout'),
		url(r'^camisetas/page/(?P<pagina>.*)/$', 'camisetas_view', name = 'vista_camisetas'),
		url(r'^registro/$','register_view', name = 'vista_registro'),


)

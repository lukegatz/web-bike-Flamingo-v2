"""flamingo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from loja import views

'''
Arquivo central de dispatch. Aqui estão listados os paths para as diversas áreas 
do site.
Os padrões aqui definidos renderizam a view respectiva ou enviam requisição para 
a view específica (chamada por meio do include).
'''
urlpatterns = [
    path('grappelli/', include('grappelli.urls')),  # grappelli URLS
    path('', views.home, name='homepage'),
    path('admin/', admin.site.urls),
    # path('hello/', views.hello), # 'ola mundo!!' (apenas para teste)
    path('clientes/', include('clientes.urls')),
    path('blog/', include('blog.urls')),
    path(r'produtos/', include('produtos.urls')),
    path('mapas/', include('mapas.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# personalizações do admin
admin.site.index_title = "Bike Flamingo"
admin.site.site_header = "LOGIN :: Bike Flamingo"
admin.site.site_title = "Bike Flamingo"
"""django_portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from portfolio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',  views.home, name='home'),

    path('registrar/', views.registrar, name='registrar'),
    path('cerrarSeccion/', views.cerrarSeccion, name='cerrarSeccion'),
    path('iniciarSeccion/', views.iniciarSeccion, name='iniciarSeccion'),

    path('blog/', include('blog.urls')),


    path('educacion/', views.educacion_list, name='educacion_list'),
    path('educacion/nueva/', views.educacion_create, name='educacion_create'),
    path('educacion/<int:pk>/editar/', views.educacion_update, name='educacion_update'),
    path('educacion/<int:pk>/eliminar/', views.educacion_delete, name='educacion_delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

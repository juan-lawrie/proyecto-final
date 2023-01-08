"""project URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from django.views.generic import TemplateView
from ejemplo.views import (index, saludar_a, sumar, 
                            buscar, monstrar_familiares,
                            BuscarFamiliar, AltaFamiliar,
                            ActualizarFamiliar, BorrarFamiliar,
                            FamiliarList, FamiliarCrear, FamiliarBorrar, FamiliarActualizar, FamiliarDetalle)
from Trabajo_final.views import (index, PostDetalle, PostListar, 
                               PostCrear, PostBorrar, PostActualizar,
                               UserSignUp, UserLogin, UserLogout, 
                               AvatarActualizar, UserActualizar, MensajeCrear, MensajeListar, MensajeDetalle, About )
from django.contrib.admin.views.decorators import staff_member_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludar/', index),
    path('saludar-a/<nombre>/', saludar_a),
    path('sumar/<int:a>/<int:b>/', sumar),
    path('buscar/',buscar),
    path('mi-familia/', monstrar_familiares),
    path('mi-familia/buscar', BuscarFamiliar.as_view()),
    path('mi-familia/alta', AltaFamiliar.as_view()),
    path('mi-familia/actualizar/<int:pk>', ActualizarFamiliar.as_view()),
    path('mi-familia/borrar/<int:pk>', BorrarFamiliar.as_view()),
    path('panel-familia/', FamiliarList.as_view()),
    path('panel-familia/crear', FamiliarCrear.as_view()),
    path('panel-familia/<int:pk>/borrar', FamiliarBorrar.as_view()),
    path('panel-familia/<int:pk>/actualizar', FamiliarActualizar.as_view()),
    path('panel-familia/<int:pk>/detalle', FamiliarDetalle.as_view()),
    path('success_updated_message/',TemplateView.as_view(template_name="ejemplo/success_updated_message.html")),
    path('Trabajo-final/', index, name="Trabajo-final-index"),
    path('Trabajo-final/<int:pk>/detalle/', PostDetalle.as_view(), name="Trabajo-final-detalle"),
    path('Trabajo-final/listar/', PostListar.as_view(), name="Trabajo-final-listar"),
    path('Trabajo-final/crear/', staff_member_required(PostCrear.as_view()), name="Trabajo-final-crear"),
    path('Trabajo-final/<int:pk>/borrar/', staff_member_required(PostBorrar.as_view()), name="Trabajo-final-borrar"),
    path('Trabajo-final/<int:pk>/actualizar/', staff_member_required(PostActualizar.as_view()), name="Trabajo-final-actualizar"),
    path('Trabajo-final/signup/', UserSignUp.as_view(), name ="Trabajo-final-signup"),
    path('Trabajo-final/login/', UserLogin.as_view(), name= "Trabajo-final-login"),
    path('Trabajo-final/logout/', UserLogout.as_view(), name="Trabajo-final-logout"),
    path('Trabajo-final/avatars/<int:pk>/actualizar/', AvatarActualizar.as_view(), name="Trabajo-final-avatars-actualizar"),
    path('Trabajo-final/users/<int:pk>/actualizar/', UserActualizar.as_view(), name="Trabajo-final-users-actualizar"),
    path('Trabajo-final/mensajes/crear/', MensajeCrear.as_view(), name="Trabajo-final-mensajes-crear"),
    path('Trabajo-final/mensajes/<int:pk>/detalle/', MensajeDetalle.as_view(), name="Trabajo-final-mensajes-detalle"),
    path('Trabajo-final/mensajes/listar/', MensajeListar.as_view(), name="Trabajo-final-mensajes-listar"),
    path('Trabajo-final/about/', About, name= "Trabajo-final-about"),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
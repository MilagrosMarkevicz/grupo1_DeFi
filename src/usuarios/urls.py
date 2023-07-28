from django.urls import path

from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView

from .views import RegistroView,EditarUsuario



app_name= 'usuarios'

urlpatterns=[
    path('login/',LoginView.as_view(template_name = 'usuarios/login.html'),name = 'login'),
    path('logout/', LogoutView.as_view(next_page='../login'),name = 'logout'),
    path('registrarse/', RegistroView.as_view(),name = 'registrarse'),
    path('editar_usuario/<int:pk>', EditarUsuario.as_view(),name = 'editar_usuario'),
    path('editar_contrasenia/<int:pk>', PasswordChangeView.as_view(template_name = 'usuarios/cambiar_contrasenia.html',success_url = '../../index'), name = 'cambiar_contrasenia')
]



from django.urls import path, include
from GameMate7.views import RegistroUsuarioView, LoginUsuarioView, LogoutUsuarioView

#app_name = 'GameMate7'

urlpatterns = [
    path('registro/', RegistroUsuarioView.as_view(), name='registro'),
    path('login/', LoginUsuarioView.as_view(), name='login'),
    path('logout/', LogoutUsuarioView.as_view(), name='logout'),
     path('reset/',
         include('django_rest_passwordreset.urls',
                 namespace='password_reset')),
    # Otras rutas URL de la aplicación GameMate7...
]


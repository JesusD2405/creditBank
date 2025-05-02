from django.urls import path
from ..auth2.views import loginView, LogoutView
from ..client.views import ClientView

urlpatterns = [
    # Default Path
    path('', ClientView, name="clients_list"),
    # Auth 
    path('login', loginView, name="login"),
    path('logout', LogoutView, name='logout'),
    # Clients
    path('clients', ClientView, name="clients_list"),
    
]
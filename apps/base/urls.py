from django.urls import path, re_path
from ..auth2.views import loginView, LogoutView
from ..client.views import ClientView
from ..credit.views import CreditsView
from ..bank.views import BankView

urlpatterns = [
    # Default Path
    path('', ClientView, name="clients_list"),
    # Auth 
    re_path(r'^login/?$', loginView, name="login"),
    re_path(r'^logout/?$', LogoutView, name='logout'),
    # Clientes
    re_path(r'^clients/?$', ClientView, name="clients_list"),
    # Creditos
    re_path(r'^credits/?$', CreditsView, name="credits_list"),
    # Bancos
    re_path(r'^banks/?$', BankView, name="banks_list"),
    
]
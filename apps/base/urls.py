from django.urls import path
from ..auth2.views import loginView, LogoutView
from ..client.views import ClientView
from ..credit.views import CreditsView
from ..bank.views import BankView

urlpatterns = [
    # Default Path
    path('', ClientView, name="clients_list"),
    # Auth 
    path('login', loginView, name="login"),
    path('logout', LogoutView, name='logout'),
    # Clientes
    path('clients', ClientView, name="clients_list"),
    # Creditos
    path('credits', CreditsView, name="credits_list"),
    # Bancos
    path('banks', BankView, name="banks_list"),
    
]
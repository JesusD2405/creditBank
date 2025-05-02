from django.urls import path
from ..auth2.views import loginView, LogoutView

urlpatterns = [
    path('login', loginView, name="login"),
    path('logout', LogoutView, name='logout'),
]
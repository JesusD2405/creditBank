from django.contrib import admin
from safedelete.admin import SafeDeleteAdmin, highlight_deleted

# Modelos
from .models import *


# Usuario
@admin.register(Client)
class ClientAdmin(SafeDeleteAdmin):

    search_fields = [
        "full_name",
        "birth_date",
        "nationality",
        "address",
        "email",
    ]

    list_display  = (
        highlight_deleted, 
        "full_name",
        "birth_date",
        "nationality",
        "address",
        "email",
    ) + SafeDeleteAdmin.list_display
from django.contrib import admin
from safedelete.admin import SafeDeleteAdmin, highlight_deleted

# Modelos
from .models import *


# Banco
@admin.register(Bank)
class BankAdmin(SafeDeleteAdmin):

    search_fields = [
        "name",
        "bank_type",
        "address",
    ]

    list_display  = (
        highlight_deleted, 
        "name",
        "bank_type",
        "address",
    ) + SafeDeleteAdmin.list_display
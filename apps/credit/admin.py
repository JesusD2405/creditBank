from django.contrib import admin
from safedelete.admin import SafeDeleteAdmin, highlight_deleted

# Modelos
from .models import *


# Usuario
@admin.register(Credit)
class CreditAdmin(SafeDeleteAdmin):

    search_fields = [
        "description",
        "minimum_payment",
        "maximum_payment",
        "credit_period",
        "credit_type",
    ]

    list_display  = (
        highlight_deleted, 
        "description",
        "minimum_payment",
        "maximum_payment",
        "credit_period",
        "credit_type",
    ) + SafeDeleteAdmin.list_display
from django.db import models
from safedelete.models import SafeDeleteModel
from django.db.models import Q

from ..base.models import BaseModel


# Modelo Banco
class Bank(BaseModel, SafeDeleteModel):

    BANK_TYPE = (
        ('P', 'Privado'),
        ('G', 'Gobierno'),
    )

    name = models.CharField(max_length=150, verbose_name='Nombre') 
    bank_type = models.CharField(max_length=2, choices=BANK_TYPE, verbose_name='Tipo de Banco')
    address = models.CharField(max_length=255, verbose_name='Dirección', null=True, blank=True)

    class Meta:
        db_table = "bank"
        verbose_name = "bank"
        verbose_name_plural = "banks"

    def __str__(self):
        return self.name
from django.db import models
from safedelete.models import SafeDeleteModel
from django.db.models import Q

from ..base.models import BaseModel
from ..client.models import Client


# Modelo Crédito
class Credit(BaseModel, SafeDeleteModel):

    CREDIT_TYPE = (
        ('A', 'Automotriz'),
        ('H', 'Hipotecarios'),
        ('C', 'Comerciales'),
    )

    description = models.CharField(max_length=150, verbose_name='Descripción') 
    minimum_payment = models.FloatField(verbose_name='Pago Mínimo')
    maximum_payment = models.FloatField(verbose_name='Pago Máximo')
    credit_period = models.PositiveIntegerField(verbose_name='Plazo de Crédito (Meses)')
    credit_type = models.CharField(max_length=2, choices=CREDIT_TYPE, default="A", verbose_name='Tipo de Crédito')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Cliente')
    # bank = models.ForeignKey(Bank, on_delete=models.CASCADE, verbose_name='Banco')

    class Meta:
        db_table = "credit"
        verbose_name = "credit"
        verbose_name_plural = "credits"

    def __str__(self):
        return "Cliente: {} | Descripcion de crédito: {}".format(self.client.full_name, self.description)
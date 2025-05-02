from django.db import models
from safedelete.models import SafeDeleteModel
from django.db.models import Q

from ..base.models import BaseModel
from ..bank.models import Bank

# Modelo Cliente
class Client(BaseModel, SafeDeleteModel):

    PERSON_TYPE = (
        ('N', 'NATURAL'),
        ('J', 'JURIDICO'),
    )
    
    GENDER_TYPE = (
        ('NA', 'NO APLICA'),
        ('M', 'HOMBRE'),
        ('F', 'MUJER'),
    )

    full_name = models.CharField(max_length=150, default='', verbose_name='Nombre y Apellido') 
    birth_date = models.DateField(verbose_name='Fecha de Nacimiento')
    nationality = models.CharField(max_length=150, verbose_name='Nacionalidad', null=True, blank=True) 
    address = models.CharField(max_length=255, verbose_name='Dirección de habitación', null=True, blank=True)
    email = models.EmailField(max_length=255, verbose_name='Correo Electrónico')
    phone_prefix = models.CharField(max_length=4, verbose_name='Prefijo de Tlf (+58)', null=True, blank=True)
    phone = models.CharField(max_length=255, verbose_name='Teléfono', null=True, blank=True)
    person_type = models.CharField(max_length=1, choices=PERSON_TYPE, default='N', verbose_name='Tipo de Persona')
    gender = models.CharField(max_length=2, choices=GENDER_TYPE, verbose_name='Género')
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, verbose_name='Banco')

    class Meta:
        db_table = "client"
        verbose_name = "client"
        verbose_name_plural = "clients"
        constraints = [
            models.UniqueConstraint(
                fields=['email', 'deleted'],
                condition=Q(deleted__isnull=False),
                name='clients_email_key'
            ),
        ]

    def __str__(self):
        return self.full_name
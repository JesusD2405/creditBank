import uuid
from django.db import models
from safedelete.models import SOFT_DELETE_CASCADE


# Modelo Base
class BaseModel(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    created_at = models.DateTimeField(verbose_name='Fecha de Creación', null=True, editable=False, auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Fecha de Actualización', auto_now=True, editable=False)
    _safedelete_policy  = SOFT_DELETE_CASCADE
    
    class Meta:
        abstract = True
        verbose_name = "Base Model"
        verbose_name_plural = "Base Models"


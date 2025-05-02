from rest_framework import serializers

# Modelos
from .models import *

# Serializadores
from ..client.serializers import ClientSerializer

# Crédito
class CreditSerializer(serializers.ModelSerializer):
    client = ClientSerializer()

    class Meta:
        model = Credit
        exclude = [
            'deleted',
            'deleted_by_cascade',
        ]
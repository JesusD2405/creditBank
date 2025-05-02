from rest_framework import serializers

# Modelos
from .models import *

# Clientes
class ClientSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField()

    class Meta:
        model = Client
        exclude = [
            'deleted',
            'deleted_by_cascade',
        ]
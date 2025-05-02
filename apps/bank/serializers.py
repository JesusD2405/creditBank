from rest_framework import serializers

# Modelos
from .models import *

# Banco
class BankSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = Bank
        exclude = [
            'deleted',
            'deleted_by_cascade',
        ]
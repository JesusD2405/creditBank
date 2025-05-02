from rest_framework import serializers

# Modelos
from .models import *
from ..client.models import Client

# Serializadores
from ..client.serializers import ClientSerializer
from ..bank.serializers import BankSerializer

# Crédito
class CreditSerializer(serializers.ModelSerializer):
    client = ClientSerializer(read_only=True)
    client_id = serializers.UUIDField()
    bank = BankSerializer(read_only=True)
    bank_id = serializers.UUIDField()

    class Meta:
        model = Credit
        exclude = [
            'deleted',
            'deleted_by_cascade',
        ]
        
    def validate(self, data):
        bank = Bank.objects.get(id=data['bank_id'])
        if bank is None:
          raise serializers.ValidationError('Bank not found.')

        data['bank'] = bank
        
        client = Client.objects.get(id=data['client_id'])
        if client is None:
          raise serializers.ValidationError('Client not found.')

        return data
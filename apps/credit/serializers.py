from rest_framework import serializers

# Modelos
from .models import *
from ..client.models import Client

# Serializadores
from ..client.serializers import ClientSerializer
from ..bank.serializers import BankSerializer

# Crédito
class CreditSerializer(serializers.ModelSerializer):
    client = ClientSerializer()
    bank = BankSerializer()

    class Meta:
        model = Credit
        exclude = [
            'deleted',
            'deleted_by_cascade',
        ]
    
    def create(self, validated_data):
        try:
            bank_data = validated_data.pop('bank')
            client_data = validated_data.pop('client')
            
            bank = Bank.objects.get(id=bank_data['id'])
            client = Client.objects.get(id=client_data['id'])
            
            return Credit.objects.create(
                bank=bank,
                client=client,
                **validated_data
            )
        except KeyError as e:
            raise serializers.ValidationError(f'Falta campo requerido: {str(e)}')
        except (Bank.DoesNotExist, Client.DoesNotExist):
            raise serializers.ValidationError('Banco o Cliente no existe')
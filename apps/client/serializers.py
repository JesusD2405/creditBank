from rest_framework import serializers

# Modelos
from .models import *

from ..bank.serializers import BankSerializer

# Clientes
class ClientSerializer(serializers.ModelSerializer):
    
    bank = BankSerializer(read_only=True)
    bank_id = serializers.UUIDField()

    class Meta:
        model = Client
        exclude = [
            'deleted',
            'deleted_by_cascade',
        ]
    
    def create(self, validated_data):
        if Client.objects.filter(email = validated_data['email'].lower()).first():
            raise serializers.ValidationError("¡El email ya se encuentra registrado!")

        return Client.objects.create(**validated_data)


    def update(self, instance, validated_data):
        if instance.email.lower() != validated_data['email'] and Client.objects.filter(email = validated_data['email'].lower()).first():
            raise serializers.ValidationError("¡El email ya se encuentra registrado!")

        instance.full_name = validated_data['full_name']
        instance.birth_date = validated_data['birth_date']
        instance.nationality = validated_data['nationality']
        instance.address = validated_data['address']
        instance.email = validated_data['email']
        instance.phone_prefix = validated_data['phone_prefix']
        instance.phone = validated_data['phone']
        instance.person_type = validated_data['person_type']
        instance.gender = validated_data['gender']
        instance.bank = validated_data['bank']
        instance.save()

        return instance


    def validate(self, data):
        bank = Bank.objects.get(id=data['bank_id'])
        if bank is None:
          raise serializers.ValidationError('Bank not found.')

        data['bank'] = bank

        return data
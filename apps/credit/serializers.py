from rest_framework import serializers

# Modelos
from .models import *

# Crédito
class CreditSerializer(serializers.ModelSerializer):

    class Meta:
        model = Credit
        exclude = [
            'deleted',
            'deleted_by_cascade',
        ]
from rest_framework import serializers
from django.contrib.auth import get_user_model

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
from rest_framework import serializers
from django.contrib.auth import get_user_model

# Modelos
from .models import *

# Clientes
class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        exclude = [
            'deleted',
            'deleted_by_cascade',
        ]
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

# Serializadores
from .serializers import *

#Modelos
from .models import *

class CreditViewSet(viewsets.ModelViewSet):
	queryset = Credit.objects.all()
	serializer_class = CreditSerializer
	filter_backends = [
		DjangoFilterBackend,
		filters.SearchFilter,
		filters.OrderingFilter
	]
	search_fields = [
    	'description',
		'minimum_payment',
		'maximum_payment',
		'credit_period',
		'credit_type'
  	]
	ordering_fields = '__all__'

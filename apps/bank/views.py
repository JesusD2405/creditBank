from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

# Serializadores
from .serializers import *

#Modelos
from .models import *

class BankViewSet(viewsets.ModelViewSet):
	queryset = Bank.objects.all()
	serializer_class = BankSerializer
	filter_backends = [
		DjangoFilterBackend,
		filters.SearchFilter,
		filters.OrderingFilter
	]
	search_fields = [
    	"name",
        "bank_type",
        "address"
  	]
	ordering_fields = '__all__'

from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

# Serializadores
from .serializers import *

#Modelos
from .models import *

class ClientViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Client.objects.all()
	serializer_class = ClientSerializer
	filter_backends = [
		DjangoFilterBackend,
		filters.SearchFilter,
		filters.OrderingFilter
	]
	search_fields = ['first_name', 'last_name', 'email', 'city', 'phone', 'document']
	ordering_fields = '__all__'

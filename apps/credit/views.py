from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view, renderer_classes
from rest_framework import filters
from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer


# Serializadores
from .serializers import *

#Modelos
from .models import *

# Vista - Listado de Créditos
@swagger_auto_schema(method='GET', auto_schema=None)
@login_required(login_url='/login/')
@api_view(['GET'])
@renderer_classes([TemplateHTMLRenderer])
def CreditsView(request):
    return Response({}, template_name= 'admin/credit_list.html')

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

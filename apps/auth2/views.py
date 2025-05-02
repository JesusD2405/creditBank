from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes, api_view, renderer_classes
from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate, logout

# Serializadores
from .serializers import *

#Modelos
from .models import *

import logging
logger = logging.getLogger( __name__ )

# Login View
# @swagger_auto_schema(methods=['GET', 'POST'], auto_schema=None)
@api_view(['GET', 'POST'])
@renderer_classes([TemplateHTMLRenderer])
@permission_classes([AllowAny])
def loginView(request):
    logger.info('Details access to the login: {}'.format(request.META['HTTP_USER_AGENT']))
    if request.method == 'POST':
        user = authenticate(request, username=request.data['username'],password=request.data['password'])
        if user:
            login(request, user)
            # TODO: Redireccionar a la vista (por definir)
            return redirect('')
        message_error = '¡Usuario o Contraseña Inválida!'
        return Response({'message_error': message_error }, template_name= 'login.html')

    # TODO: Falta crear vista de login
    return Response({}, template_name= 'login.html')


# Logout View
# @swagger_auto_schema(method='GET', auto_schema=None)
@api_view(['GET'])
@permission_classes([AllowAny])
def LogoutView(request):
    logout(request)
    return redirect('login')

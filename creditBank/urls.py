from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls.static import static

schema_view = get_schema_view(
   openapi.Info(
      title="Credit Bank API",
      default_version='v1',
      description="API para gestión de procesos de ....",
      contact=openapi.Contact(email="jesusdavid2405@gmail.com"),
    #   terms_of_service="https://www.google.com/policies/terms/",
    #   license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('api/', include('api.urls')),
    path(settings.ADMIN_URL, admin.site.urls),
]

urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

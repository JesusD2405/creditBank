from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Create a router and register our viewsets with it.
router = DefaultRouter()


# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
	path('', include(router.urls)),
	path('auth/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

from django.urls import path, include
from rest_framework import routers
from .views import AddressViewSet

# Define the router
router = routers.DefaultRouter()
router.register(r'address', AddressViewSet)

# Define the urlpatterns
urlpatterns = [
    path('', include(router.urls)),
]

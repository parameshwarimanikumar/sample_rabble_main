# address/serializers.py

from rest_framework import serializers
from .models import Address

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id','profile', 'street', 'city', 'state', 'country', 'postal_code', 'address_line']

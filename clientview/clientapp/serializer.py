from rest_framework import serializers
from .models import ClientRequest
from .models import TxnList

class ClientRequestSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = ClientRequest
        fields = ('sender', 'receiver','message')
        #read_only_fields = ('txnid','sender','blockid','hashofblock','date_created')


class TxnListSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = TxnList
        fields = ('txnid', 'sender', 'receiver','message', 'blockid','hashofblock', 'date_created')
from rest_framework import serializers
from .models import ClientList
from .models import BlockList
from .models import Object

class ClientListSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = ClientList
        fields = ('txnid', 'sender', 'receiver','message', 'blockid','hashofblock', 'date_created')
        #read_only_fields = ('txnid','sender','blockid','hashofblock','date_created')

class BlockListSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = BlockList
        fields = ('hashofblock','blockid', 'nooftxn', 'hashprev','txn', 'time_created')


class ObjectSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Object
        fields = ('block',)
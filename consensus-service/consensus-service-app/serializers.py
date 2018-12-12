from rest_framework import serializers
from .models import Txn
from .models import BlockList

class StorelistSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Txn
        fields = ('txnid', 'sender', 'receiver','message', 'blockid','hashofblock', 'date_created')
 
class BlockListSerializer(serializers.ModelSerializer):

    class Meta:
    	model = BlockList
    	fields = ('hashofblock','blockid', 'nooftxn', 'hashprev','txn', 'time_created')
from django.db import models
from django.db.models.fields import IntegerField
from django.contrib.postgres.fields import ArrayField

class ClientList(models.Model):
    """This class represents the bucketlist model."""

    def contact_default():
    	return {"email": "to1@example.com"}

    txnid = models.CharField(max_length=256, blank=False,default = "0", unique=True)
    sender = models.CharField(max_length=256, blank=False, default=contact_default)
    receiver = models.CharField(max_length=256, blank=False, default=contact_default)
    message = models.CharField(max_length=256, blank=False, default=contact_default)
    blockid = models.PositiveIntegerField(default = 0)
    hashofblock= models.CharField(max_length=256, default=0)

    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.txnid)

class BlockList(models.Model):

    hashofblock = models.CharField(max_length=256, default=0, unique=True)
    blockid = models.PositiveIntegerField(default=0)
    nooftxn = models.PositiveIntegerField(default=0)
    hashprev = models.CharField(max_length=256, blank=False, unique = True)
    txn = ArrayField(models.CharField(max_length=256, blank=False),size=4)

    time_created = models.DateTimeField(auto_now_add=True)

class  Object(models.Model):

    def contact_default():
        return {"email": "to1@example.com"}

    block = models.CharField(max_length=1024, blank=False,  default=contact_default)
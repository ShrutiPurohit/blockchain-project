from django.db import models
from django.db.models.fields import IntegerField



class ClientRequest(models.Model):
    """This class represents the bucketlist model."""

    def contact_default():
    	return {"email": "to1@example.com"}

    #txnid = models.CharField(max_length=256, blank=False,default = "0", unique=True)
    sender = models.CharField(max_length=256, blank=False, default=contact_default)
    receiver = models.CharField(max_length=256, blank=False, default=contact_default)
    message = models.CharField(max_length=256, blank=False, default=contact_default)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.txnid)


class TxnList(models.Model):

	def contact_default():
		return {"email": "to1@example.com"}

	txnid = models.CharField(max_length=256, blank=False, default=contact_default)
	sender = models.CharField(max_length=256, blank=False, default=contact_default)
	receiver = models.CharField(max_length=256, blank=False, default=contact_default)
	message = models.CharField(max_length=256, blank=False, default=contact_default)
	blockid = models.PositiveIntegerField(default = 0)
	hashofblock= models.CharField(max_length=256, default=0)
    
	date_created = models.CharField(max_length=256, blank=False, default=contact_default)

	def __str__(self):
		return "{}".format(self.txnid)
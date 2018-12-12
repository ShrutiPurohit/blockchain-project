from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView
from .views import RequestedTxn
from .views import GetTxns
from .views import GetSenderTxn

urlpatterns = {	

    url(r'^reqlist/$', CreateView.as_view(), name="create"),
    url(r'^txndetails/$', RequestedTxn.as_view(), name="Response from CS"),
    url(r'^clientreq/sender/(?P<pk1>\w+)/txnid/(?P<pk2>[0-9]+)/$', GetTxns.as_view(), name="Txn Details"),
    url(r'^clientreq/sender/(?P<pk1>\w+)/$', GetSenderTxn.as_view(), name="Sender Txn Details"),

}

urlpatterns = format_suffix_patterns(urlpatterns)
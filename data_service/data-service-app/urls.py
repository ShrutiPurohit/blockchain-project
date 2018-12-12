from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView
from .views import CreateBlock
from .views import DetailsTxnid
from .views import DetailsSender
from .views import DetailsReceiver
from .views import SenderReceiver
from .views import ObjectCreate

urlpatterns = {
	url(r'^blocklist/$', CreateBlock.as_view(), name="create blocks"),

	url(r'^blockobj/$', ObjectCreate.as_view(), name="block object"),

    url(r'^clientlist/$', CreateView.as_view(), name="create"),

    url(r'^clientlist/sender/(?P<pk1>\w+)/txnid/(?P<pk2>[0-9]+)/$', DetailsTxnid.as_view(), name="details"),

    url(r'^clientlist/sender/(?P<pk>\w+)/$', DetailsSender.as_view(), name="details"),

    url(r'^clientlist/receiver/(?P<pk>\w+)/$', DetailsReceiver.as_view(), name="details"),

    url(r'^clientlist/sender/(?P<pk1>\w+)/receiver/(?P<pk2>\w+)/$', SenderReceiver.as_view(), name="details"),

}

urlpatterns = format_suffix_patterns(urlpatterns)
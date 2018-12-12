from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
#from .views import Store
#from .views import Send
from .views import Show
from .views import CreateBlock

urlpatterns = {
	#url(r'^storelist/store/$', Store.as_view(), name="store txns"),
	#url(r'^storelist/send/$', Send.as_view(), name="send txns"),
	url(r'^storelist/show/$', Show.as_view(), name="show txns"),
	url(r'^blocklist/$', CreateBlock.as_view(), name=" Create block"),
	#url(r'', Store.home, name='home'),

}

urlpatterns = format_suffix_patterns(urlpatterns)
from django.conf.urls import url,include
from rest_framework.urlpatterns import format_suffix_patterns
#from .views import StockList StockDetail
from rest_framework import routers
from .views import TaskViewSet,ConfigViewSet


from rest_framework_extensions.routers import ExtendedSimpleRouter

router=ExtendedSimpleRouter()
(
	router.register(r'stock',TaskViewSet,base_name='stock')
		.register(r'config',ConfigViewSet,base_name='config',parents_query_lookups=['id'])
	)


urlpatterns=router.urls
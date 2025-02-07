from netbox.api.routers import NetBoxRouter
from . import views


router = NetBoxRouter()

router.register('gns3server', views.GNS3ServerViewSet, basename='gns3server')
router.register('ptovjob', views.ptovjobViewSet, basename='ptovjob')
router.register('switchtojob', views.switchtojobViewSet, basename='switchtojob')

urlpatterns = router.urls

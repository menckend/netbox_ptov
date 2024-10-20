from netbox.api.routers import NetBoxRouter

from .views import (
    gns3srvViewSet, ptovjobViewSet, switchtojobViewSet, RootView
)

app_name = 'netbox_ptov'

router = NetBoxRouter()
router.APIRootView = RootView
router.register('gns3srv', gns3srvViewSet, basename='gns3srv')
router.register('ptovjob', ptovjobViewSet, basename='ptovjob')
router.register('switchtojob', switchtojobViewSet, basename='switchtojob')

urlpatterns = router.urls

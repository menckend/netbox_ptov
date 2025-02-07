from netbox.api.viewsets import NetBoxModelViewSet
from netbox_ptov import filtersets, models
from netbox_ptov.api.serializers import (
    GNS3ServerSerializer, ptovjobSerializer, switchtojobSerializer
)


class GNS3ServerViewSet(NetBoxModelViewSet):
    queryset = models.GNS3Server.objects.all()
    serializer_class = GNS3ServerSerializer
    filterset_class = filtersets.GNS3ServerFilterSet


class ptovjobViewSet(NetBoxModelViewSet):
    queryset = models.ptovjob.objects.all()
    serializer_class = ptovjobSerializer
    filterset_class = filtersets.ptovjobFilterSet


class switchtojobViewSet(NetBoxModelViewSet):
    queryset = models.switchtojob.objects.all()
    serializer_class = switchtojobSerializer
    filterset_class = filtersets.switchtojobFilterSet

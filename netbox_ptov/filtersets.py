from netbox.filtersets import NetBoxModelFilterSet
from .models import GNS3Server, ptovjob, switchtojob


class GNS3ServerFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = GNS3Server
        fields = ['name']


class ptovjobFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = ptovjob
        fields = ['name', 'gns3prjname', 'gns3srv', 'eosuname']


class switchtojobFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = switchtojob
        fields = ['name', 'job', 'switch']

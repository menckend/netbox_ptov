from rest_framework.serializers import HyperlinkedIdentityField
from netbox.api.serializers import NetBoxModelSerializer
from netbox_ptov.models import GNS3Server, ptovjob, switchtojob


class GNS3ServerSerializer(NetBoxModelSerializer):
    url = HyperlinkedIdentityField(view_name="plugins-api:netbox_ptov:gns3server-detail")

    class Meta:
        model = GNS3Server
        fields = [
            "id", "url", "display", "name", "tags", "custom_fields", "created",
            "last_updated",
        ]


class ptovjobSerializer(NetBoxModelSerializer):
    url = HyperlinkedIdentityField(view_name="plugins-api:netbox_ptov:ptovjob-detail")

    class Meta:
        model = ptovjob
        fields = [
            "id", "url", "display", "name", "eosuname", "gns3srv", "gns3prjname", 
            "gns3prjid", "eospasswd", "tags", "custom_fields", "created", "last_updated"
        ]


class switchtojobSerializer(NetBoxModelSerializer):
    url = HyperlinkedIdentityField(view_name="plugins-api:netbox_ptov:switchtojob-detail")

    class Meta:
        model = switchtojob
        fields = [
            "id", "url", "display", "name", "job", "switch", "tags", "custom_fields",
            "created", "last_updated"
        ]

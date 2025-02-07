from netbox.tables import NetBoxTable
from .models import GNS3Server, ptovjob, switchtojob


class GNS3ServerTable(NetBoxTable):
    """A class to represent the GNS3 servers table."""
    class Meta(NetBoxTable.Meta):
        model = GNS3Server
        fields = ("pk", "id", "name", "actions")
        default_columns = ("name",)


class ptovjobTable(NetBoxTable):
    """A class to represent the ptovjob table."""
    class Meta(NetBoxTable.Meta):
        model = ptovjob
        fields = ("pk", "id", "name", "gns3srv", "gns3prjname", "gns3prjid", "eosuname", "eospasswd")
        default_columns = ("name",)


class switchtojobTable(NetBoxTable):
    """A class to represent the switchtojob table."""
    class Meta(NetBoxTable.Meta):
        model = switchtojob
        fields = ("pk", "id", "name", "job", "switch")
        default_columns = ("name",)

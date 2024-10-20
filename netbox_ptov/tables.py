import django_tables2 as tables
from netbox.tables import NetBoxTable, ChoiceFieldColumn

from .models import gns3srv, ptovjob, switchtojob


#class ptovTable(NetBoxTable):
#    name = tables.Column(linkify=True)
#
#    class Meta(NetBoxTable.Meta):
#        model = ptov
#        fields = ("pk", "id", "name", "actions")
#        default_columns = ("name",)

class gns3srvTable(NetBoxTable):
    name = tables.Column(linkify=True)

    class Meta(NetBoxTable.Meta):
        model = gns3srv 
        fields = ("pk", "id", "name", "actions")
        default_columns = ("name",)

class ptovjobTable(NetBoxTable):
    name = tables.Column(linkify=True)

    class Meta(NetBoxTable.Meta):
        model = ptovjob
        fields = ("pk", "id", "name", "gns3srv", "gns3prjname", "gns3prjid", "eosuname", "eospasswd")
        default_columns = ("name",)

class switchtojobTable(NetBoxTable):
    name = tables.Column(linkify=True)

    class Meta(NetBoxTable.Meta):
        model = switchtojob
        fields = ("pk", "id", 'name', "job", "switch")
        default_columns = ("name",)

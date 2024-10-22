from rest_framework import serializers

from netbox.api.serializersbase import *
from netbox.api.serializersfeatures import *
from netbox.api.serializersgeneric import *
from netbox.api.serializersnested import *


#
# Base model serializers
#

class NetBoxModelSerializer(TaggableModelSerializer, CustomFieldModelSerializer, ValidatedModelSerializer):
    """
    Adds support for custom fields and tags.
    """
    pass


class NestedGroupModelSerializer(NetBoxModelSerializer):
    """
    Extends PrimaryModelSerializer to include MPTT support.
    """
    _depth = serializers.IntegerField(source='level', read_only=True)


class BulkOperationSerializer(serializers.Serializer):
    id = serializers.IntegerField()

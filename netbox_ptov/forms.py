from django import forms
# from ipam.models import Prefix
from netbox.forms import NetBoxModelForm  ##, NetBoxModelFilterSetForm
# from utilities.forms.fields import CommentField, DynamicModelChoiceField
from dcim.models import devices
from .models import gns3srv, ptovjob, switchtojob


class gns3srvForm(NetBoxModelForm):
    class Meta:
        model = gns3srv
        fields = ("name", "tags")


class ptovjobForm(NetBoxModelForm):
    class Meta:
        model = ptovjob
        fields = ("name", "gns3srv", "gns3prjname", "gns3prjid", "eosuname", "eospasswd")


class switchtojobForm(NetBoxModelForm):
    class Meta:
        model = switchtojob
        fields = ("name", "switch", "job")


class golabForm(forms.Form):
    username_in = forms.CharField(label="Enter EOS username:", widget=forms.TextInput)
    password_in = forms.CharField(label="Enter EOS password:", widget=forms.PasswordInput)
    switchlist_multiplechoice_in = forms.ModelMultipleChoiceField(queryset=devices.Device.objects.filter(device_type__manufacturer__slug="arista"), to_field_name='name')
    serverselect_in = forms.ModelChoiceField(queryset=gns3srv.objects.all(), to_field_name='name')
    prjname_in = forms.CharField(label="Enter Name for GNS3 project:", widget=forms.TextInput)

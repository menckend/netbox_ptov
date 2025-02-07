from django import forms
from netbox.forms import NetBoxModelForm
from dcim.models import devices
from .models import GNS3Server, ptovjob, switchtojob


class GNS3ServerForm(NetBoxModelForm):
    """A class to represent the Django form for GNS3Server"""

    class Meta:
        model = GNS3Server
        fields = ("name", "tags")


class ptovjobForm(NetBoxModelForm):
    """A class to represent the Django form for `ptovjob` """

    class Meta:
        model = ptovjob
        fields = ("name", "gns3srv", "gns3prjname", "gns3prjid", "eosuname", "eospasswd")


class switchtojobForm(NetBoxModelForm):
    """A class to represent the Django form for `switchtojob` """

    class Meta:
        model = switchtojob
        fields = ("name", "job", "switch")


class golabForm(forms.Form):
    """A class to represent the Django form for `golab` """
    username_in = forms.CharField(label="Enter EOS username:", widget=forms.TextInput)
    password_in = forms.CharField(label="Enter EOS password:", widget=forms.PasswordInput)
    switchlist_multiplechoice_in = forms.ModelMultipleChoiceField(
        label="Select the Arista switches to include in your virtual-lab", 
        queryset=devices.Device.objects.filter(device_type__manufacturer__slug="arista"), 
        to_field_name='name'
    )
    serverselect_in = forms.ModelChoiceField(
        label="Select the GNS3 server to create your virtual-lab on", 
        queryset=GNS3Server.objects.all(), 
        to_field_name='name'
    )
    prjname_in = forms.CharField(label="Enter Name for GNS3 project:", widget=forms.TextInput)

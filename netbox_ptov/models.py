"""Django models for netbox_ptov plugin

Defines the Django models used by the netbox_ptov plugin"""

from django.db import models
from django.urls import reverse
from netbox.models import NetBoxModel


class GNS3Server(NetBoxModel):
    """
    A class to represent the Django model of GNS3 servers.

    ...

    Attributes
    ----------
    name
    """

    name = models.CharField(max_length=100)

    class Meta:
        ordering = ("name",)
        

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("plugins:netbox_ptov:gns3server", args=[self.pk])


class switchtojob(NetBoxModel):
    """
    A class to represent the Django model of the list/table of `ptovjobs` <> `switch` pairs.  Each instance reflects that the specified `switch` was in-scope for the specified virtual-lab `job`

    ...

    Attributes
    ----------
    name
    """

    name = models.CharField(max_length=100)
    
    class Meta:
        ordering = ("name",)
        # unique_together = ['job', 'switch']


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("plugins:netbox_ptov:switchtojob", args=[self.pk])

    job = models.ForeignKey(
        to='netbox_ptov.PtovJob',
        on_delete=models.CASCADE,
    )

    switch = models.ForeignKey(
	to='dcim.device',
        on_delete=models.CASCADE,
    )

class ptovjob(NetBoxModel):
    """
    A class to represent the Django model virtual-labs requested through the netbox_ptov plugin

    ...

    Attributes
    ----------
    name
    gns3srv : str
    gns3prjname : str
    gns3prjid : str
    eosuname : str
    eospasswd : str
    """

    name = models.CharField(max_length=100)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("plugins:netbox_ptov:ptovjob", args=[self.pk])

    gns3srv = models.ForeignKey(
        to='netbox_ptov.GNS3Server',
        on_delete=models.CASCADE,
    )

    gns3prjname = models.CharField(max_length=100)

    gns3prjid = models.CharField(max_length=200)

    eosuname = models.CharField(max_length=100)

    eospasswd = models.CharField(max_length=100)

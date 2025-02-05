"""Defines the 'views' used by the Django apps for serving pages of the netbox_ptov plugin"""

import django
from ptovnetlab import ptovnetlab as ptvnl
from netbox.views import generic
from netbox_ptov import filtersets, forms, models, tables
from netbox_ptov.models import gns3srv
from django.shortcuts import render, redirect
from django.contrib import messages
import json
import logging


class MessagesHandler(logging.Handler):
    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    def emit(self, record):
        try:
            msg = self.format(record)
            messages.info(self.request, msg)
        except Exception:
            self.handleError(record)


def golab(request: forms.golabForm) -> django.http.HttpResponse:
    """Pass the input fields from the golabForm instance to a background job that executes the ptovnetlab.p_to_v function"""
    if request.method == 'POST':
        form = forms.golabForm(request.POST)
        if form.is_valid():
            # Extract form data
            username = form.cleaned_data['username_in']
            password = form.cleaned_data['password_in']
            switchlist = [str(swname) for swname in form.cleaned_data['switchlist_multiplechoice_in']]
            servername = form.cleaned_data['serverselect_in'].name
            projectname = form.cleaned_data['prjname_in']

            # Log initial info
            messages.add_message(request, messages.INFO, f'Switch-list: {switchlist}')
            messages.add_message(request, messages.INFO, f'GNS3 server: {servername}')

            # Create and start background job
            from .jobs import PToVJob
            job = PToVJob()
            job.start(
                request=request,
                username=username,
                password=password,
                switchlist=switchlist,
                servername=servername,
                prjname=projectname
            )
            job.save()

            # Queue the job for background execution
            job.enqueue()

            messages.add_message(
                request, 
                messages.SUCCESS, 
                f'Virtual lab creation started in background. View progress in the <a href="{job.get_absolute_url()}">Jobs</a> section.',
                extra_tags='safe'
            )
            return render(request, 'golab.html', {'form': form})
    else:
        form = forms.golabForm()
        return render(request, 'golab.html', {'form': form})

class gns3srvView(generic.ObjectView):
    """A class to represent the generic view of a gns3srv object."""

    queryset = models.gns3srv.objects.all()


class gns3srvListView(generic.ObjectListView):
    """A class to represent the view of all gns3srv objects."""

    queryset = models.gns3srv.objects.all()
    table = tables.gns3srvTable


class gns3srvEditView(generic.ObjectEditView):
    """A class to represent the edit view of a gns3srv object.
    =============================================================

    Attributes
    ----------
    queryset
    form
    """
    queryset = models.gns3srv.objects.all()
    form = forms.gns3srvForm


class gns3srvDeleteView(generic.ObjectDeleteView):
    """A class to represent the delete view of a gns3srv object.
    =============================================================
    ...

    Attributes
    ----------
    queryset
    """
    queryset = models.gns3srv.objects.all()


class ptovjobView(generic.ObjectView):
    """
    A class to represent the generic view of all ptovjob objects.

    =============================================================

    Attributes
    ----------
    queryset
    """
    queryset = models.ptovjob.objects.all()


class ptovjobListView(generic.ObjectListView):
    """
    A class to represent the list view of all ptovjob objects.

    =============================================================

    Attributes
    ----------
    queryset
    table
    """
    queryset = models.ptovjob.objects.all()
    table = tables.ptovjobTable


class ptovjobEditView(generic.ObjectEditView):
    """
    A class to represent the edit view of a ptovjob object.

    =============================================================

    Attributes
    ----------
    queryset
    form
    """
    queryset = models.ptovjob.objects.all()
    form = forms.ptovjobForm


class ptovjobDeleteView(generic.ObjectDeleteView):
    """
    A class to represent the delete  view of a ptovjob object.

    =============================================================

    Attributes
    ----------
    queryset
    """

    queryset = models.ptovjob.objects.all()


class switchtojobView(generic.ObjectView):
    """
    A class to represent the generic view of all switchtojob objects.

    =============================================================

    Attributes
    ----------
    queryset
    """
    queryset = models.switchtojob.objects.all()


class switchtojobListView(generic.ObjectListView):
    """
    A class to represent the list view of all switchtojob objects.

    =============================================================

    Attributes
    ----------
    queryset
    table
    """

    queryset = models.switchtojob.objects.all()
    table = tables.switchtojobTable


class switchtojobEditView(generic.ObjectEditView):
    """
    A class to represent the edit view of switchtojob objects.

    =============================================================

    Attributes
    =============================================================
    queryset
    form
    """

    queryset = models.switchtojob.objects.all()
    form = forms.switchtojobForm


class switchtojobDeleteView(generic.ObjectDeleteView):
    """
    A class to represent the delete view of a switchtojob object.

    =============================================================

    Attributes
    ----------
    queryset
    """

    queryset = models.switchtojob.objects.all()

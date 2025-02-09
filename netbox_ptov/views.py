"""Defines the 'views' used by the Django apps for serving pages of the netbox_ptov plugin"""

import django
from ptovnetlab import ptovnetlab as ptvnl
from netbox.views import generic
from netbox_ptov import filtersets, forms, models, tables
from netbox_ptov.models import GNS3Server
from django.shortcuts import render, redirect
from django.contrib import messages
import json
import logging
from .jobs import ptovJob
from django.shortcuts import get_object_or_404
from dcim.models import Device
import time as t
from datetime import datetime


def golab(request: forms.golabForm) -> django.http.HttpResponse:
    """Pass the input fields from the golabForm instance to the ptovnetlab.p_to_v function and return the results as an HttpResponse"""
    
    if request.method == 'POST':
        form = forms.golabForm(request.POST)
        joburl=''
        if form.is_valid():
            username = form.cleaned_data['username_in']
            password = form.cleaned_data['password_in']
            switchlist = [str(swname) for swname in form.cleaned_data['switchlist_multiplechoice_in']]
            servername = form.cleaned_data['serverselect_in'].name
            projectname = form.cleaned_data['prjname_in']

            # Log initial info
            messages.add_message(request, messages.INFO, 'Starting to poll devices and build virtual lab. This may take up to several minutes.', extra_tags='safe')

            try:
                # Call the function that does all of the work
                messages.info(request, f'Completing your request as a background job.', extra_tags='safe')
                jobtogo = ptovJob.enqueue(
                    immediate = False,
                    schedule_at = datetime.now,
                    interval = None,
                    name = 'netbox_ptov: ' + str(switchlist),
                    username = username,
                    password = password,
                    switchlist = switchlist,
                    servername = servername,
                    projectname = projectname
                )
                #joburl = ptovjob_new.get_absolute_url()
                messages.info(request, f'Job has been enqueued as: ' + str(jobtogo.name))
                return redirect(jobtogo.get_absolute_url())
                #joburl=ptovjob_new.get_absolute_url()
                #t.sleep(1)
                #return render(request, 'golab.html')
            except Exception as e:
                # Handle any exceptions and add an error message
                messages.add_message(request, messages.ERROR, f'An error occurred: {str(e)}', extra_tags='safe')
                return render(request, 'golab.html')
            finally:
                # Remove the custom handler to avoid duplicate messages in subsequent requests
                #messages.info(request, f'Still going', extra_tags='safe')
                #return render( '/core/jobs/'+ str(runningjob.pk))
                #time.sleep(3)
                #messages.info(request, f'Job has been enqueued as: ' + str(jobtogo.name))
                #messages.info(request, joburl)
                #return render(request, 'golab.html')
                #return redirect(joburl)
                #return redirect(jobtogo.get_absolute_url)
                return redirect(jobtogo.get_absolute_url())
                #pass
    else:
        form = forms.golabForm()
        return render(request, 'golab.html', {'form': form})


class GNS3ServerView(generic.ObjectView):
    """A class to represent the generic view of a GNS3Server object."""
    queryset = models.GNS3Server.objects.all()


class GNS3ServerListView(generic.ObjectListView):
    """A class to represent the view of all GNS3Server objects."""
    queryset = models.GNS3Server.objects.all()
    table = tables.GNS3ServerTable


class GNS3ServerEditView(generic.ObjectEditView):
    """A class to represent the edit view of a GNS3Server object."""
    queryset = models.GNS3Server.objects.all()
    form = forms.GNS3ServerForm


class GNS3ServerDeleteView(generic.ObjectDeleteView):
    """A class to represent the delete view of a GNS3Server object."""
    queryset = models.GNS3Server.objects.all()


class ptovjobView(generic.ObjectView):
    """A class to represent the generic view of all ptovjob objects."""
    queryset = models.ptovjob.objects.all()


class ptovjobListView(generic.ObjectListView):
    """A class to represent the list view of all ptovjob objects."""
    queryset = models.ptovjob.objects.all()
    table = tables.ptovjobTable


class ptovjobEditView(generic.ObjectEditView):
    """A class to represent the edit view of a ptovjob object."""
    queryset = models.ptovjob.objects.all()
    form = forms.ptovjobForm


class ptovjobDeleteView(generic.ObjectDeleteView):
    """A class to represent the delete view of a ptovjob object."""
    queryset = models.ptovjob.objects.all()


class switchtojobView(generic.ObjectView):
    """A class to represent the generic view of all switchtojob objects."""
    queryset = models.switchtojob.objects.all()


class switchtojobListView(generic.ObjectListView):
    """A class to represent the list view of all switchtojob objects."""
    queryset = models.switchtojob.objects.all()
    table = tables.switchtojobTable


class switchtojobEditView(generic.ObjectEditView):
    """A class to represent the edit view of switchtojob objects."""
    queryset = models.switchtojob.objects.all()
    form = forms.switchtojobForm


class switchtojobDeleteView(generic.ObjectDeleteView):
    """A class to represent the delete view of a switchtojob object."""
    queryset = models.switchtojob.objects.all()

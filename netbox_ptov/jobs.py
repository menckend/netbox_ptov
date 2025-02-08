from netbox.jobs import JobRunner
from ptovnetlab import ptovnetlab as ptvnl
from django.contrib import messages
from netbox_ptov.models import GNS3Server
import logging
from ptovnetlab import ptovnetlab as ptvnl
from netbox.views import generic
from netbox_ptov import filtersets, forms, models, tables
from django.shortcuts import render, redirect
import json


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


class ptovJob(JobRunner):
    class Meta:
        name = "ptovJob"
        #object_types = [GNS3Server]  # Changed to match the correct model name
        #verbose_name = "GNS3 Server Job"
        #description = "Creates a virtual lab from physical network devices"


    def run(self, username, password, switchlist, servername, projectname, *args, **kwargs):
        obj = self.job.object

        # Create a custom logging handler
        messages_handler = MessagesHandler(request)
        messages_handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        messages_handler.setFormatter(formatter)

        # Get the logger used by ptovnetlab.p_to_v
        logger = logging.getLogger('ptovnetlab')
        logger.addHandler(messages_handler)

        try:
            # Call the function that does all of the work
            result_out = str(ptvnl.p_to_v(
                username=username, 
                passwd=password,
                servername=servername,
                switchlist=switchlist,
                prjname=projectname
            ))
            self.log_success(f"Virtual lab created successfully: {result_out}")
            return result_out
        except Exception as e:
            self.log_failure(f"Failed to create virtual lab: {str(e)}")
            raise

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

    def __init__(self, job):
        """
        Args:
            job: The specific `Job` this `JobRunner` is executing.
        """
        self.job = job


    def run(self, **kwargs):
        obj = self.job.object

        # Create a custom logging handler
        messages_handler = MessagesHandler(obj)
        messages_handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        messages_handler.setFormatter(formatter)

        # Get the logger used by ptovnetlab.p_to_v
        logger = logging.getLogger('ptovnetlab')
        logger.addHandler(messages_handler)

        try:
            # Call the function that does all of the work
            result_out = str(ptvnl.p_to_v(
                username=kwargs['username'], 
                passwd=kwargs['password'],
                servername=kwargs['servername'],
                switchlist=kwargs['switchlist'],
                prjname=kwargs['projectname']
            ))
#            messages.add_message((f"Virtual lab created successfully: {result_out}")
            return result_out
        except Exception as e:
            messages.add_message(request, messages.ERROR, f'An error occurred: {str(e)}', extra_tags='safe')
            raise

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
from unittest.mock import MagicMock
#from asgiref.sync import sync_to_async
from django.core.management.base import BaseCommand
#import asyncio


class ptovJob(JobRunner):
    class Meta:
        name = "ptovJob"
        request = MagicMock()


    request = MagicMock()


    def __init__(self, job):
        """
        Args:
            job: The specific `Job` this `JobRunner` is executing.
        """
        self.job = job
        request = MagicMock()


    def run(self, **kwargs):
        obj = self.job.object
        request = MagicMock()

        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)

        # Create a custom handler to append logs to the job's data
        class JobDataHandler(logging.Handler):
            def __init__(self, job):
                super().__init__()
                self.job = job

            def emit(self, record):
                #log_entry = self.format(str(record))
                if not self.job.data:
                    self.job.data = []
                self.job.data.append(str(self))
                messages.info(request, str(self))
                self.job.save()  # Save the updated job data

        #class CustomFormatter(logging.Formatter):
            def formatTime(self, record, datefmt=None):
                # Ensure record.created is a float timestamp
                timestamp = self.converter(record.created)
                messages.info(request, f'timestamp: {str(timestamp)}', extra_tags='safe')
                dt_object = datetime.datetime.fromtimestamp(timestamp, tz=timezone.utc)
                messages.info(request, f'dt_object: {str(dt_object)}', extra_tags='safe')
                return dt_object.isoformat()


        logging.basicConfig(level=logging.INFO,)
            #format='%(asctime)s - %(levelname)s - %(message)s',
            #datefmt='%Y-%m-%d %H:%M:%S')
            
        handler = JobDataHandler(self.job)
        #formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        #formatter = logging.Formatter('%(message)s')
        #handler.setFormatter(formatter)
        logger.addHandler(handler)


        # Get the logger used by ptovnetlab.p_to_v
        logger2 = logging.getLogger('ptovnetlab')
        logger2.addHandler(handler)


        try:
            # Call the function that does all of the work
            result_out = str(ptvnl.p_to_v(
                username=kwargs['username'], 
                passwd=kwargs['password'],
                servername=kwargs['servername'],
                switchlist=kwargs['switchlist'],
                prjname=kwargs['projectname'],
            ))
            messages.info(request, f"Virtual lab created successfully: {result_out} (is the URL)")
            #return result_out
            return obj

        except Exception as e:
            messages.error(request, f'An error occurred running the netbox_ptov job: {str(e)}', extra_tags='safe')
            raise

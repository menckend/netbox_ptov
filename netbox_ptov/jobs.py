from netbox.jobs import JobRunner
from django.contrib import messages
from ptovnetlab import ptovnetlab as ptvnl
import logging

class PToVJob(JobRunner):
    """
    Job for executing p_to_v function in the background.
    """
    class Meta:
        name = "Create Virtual Lab"
        # description = "Creates a virtual lab in GNS3 from NetBox devices"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = None

    def start(self, request, username, password, switchlist, servername, prjname):
        """
        Initialize job with request context and parameters.
        """
        self.request = request
        self.username = username
        self.password = password
        self.switchlist = switchlist
        self.servername = servername
        self.prjname = prjname

    def run(self):
        """
        Execute the p_to_v function with job logging.
        """
        # Create a custom logging handler that forwards to both job logs and Django messages
        class MessagesHandler(logging.Handler):
            def __init__(self, job, request):
                super().__init__()
                self.job = job
                self.request = request

            def emit(self, record):
                msg = self.format(record)
                # Log to job
                self.job.log_info(msg)
                # Forward to Django messages if request exists
                if self.request:
                    messages.info(self.request, msg)

        # Set up logging
        logger = logging.getLogger('ptovnetlab')
        handler = MessagesHandler(self, self.request)
        handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        logger.addHandler(handler)

        try:
            # Execute p_to_v with provided parameters
            result = ptvnl.p_to_v(
                username=self.username,
                passwd=self.password,
                servername=self.servername,
                switchlist=self.switchlist,
                prjname=self.prjname
            )

            # Log success
            self.log_success(f"Project Created: {self.prjname} on {self.servername}")
            if result:
                self.log_info(f"Project URL: {result}")

            return result

        except Exception as e:
            # Log error and re-raise
            self.log_failure(str(e))
            raise

        finally:
            # Clean up logging
            logger.removeHandler(handler)

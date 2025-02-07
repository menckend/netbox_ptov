from netbox.jobs import JobRunner
from ptovnetlab import ptovnetlab as ptvnl
from django.contrib import messages


class ptovJob(JobRunner):
    class Meta:
        name = "ptovJob"
        object_types = ['dcim.device', 'netbox_ptov.gns3srv']
        description = "Creates a virtual lab from physical network devices"

    def run(self, username, password, switchlist, servername, projectname, *args, **kwargs):
        obj = self.job.object
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

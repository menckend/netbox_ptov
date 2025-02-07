from netbox.jobs import JobRunner


class ptovJob(JobRunner):
    class Meta:
        name = "ptovJob"

    def run(self, *args, **kwargs):
        obj = self.job.object
        # your logic goes here
        result_out = str(ptvnl.p_to_v(username=username, passwd=password , servername=servername, switchlist=switchlist, prjname=projectname))

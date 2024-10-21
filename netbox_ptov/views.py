from dcnodatg import dcnodatg
# from django.db.models import Count
from netbox.views import generic
from . import filtersets, forms, models, tables
from .models import gns3srv
from django.shortcuts import render, redirect
from django.contrib import messages
#from django.forms.models import ConfigContextModelQuerySet
import json

def golab(request):
    if request.method == 'POST':
        form = forms.golabForm(request.POST)
        if form.is_valid():
            unm = form.cleaned_data['username_in']
            pwd = form.cleaned_data['password_in']
            swl = []
            swl_in = []
            swl_in = form.cleaned_data['switchlist_multiplechoice_in']
            for swname in swl_in:
                print (swname, type(swname))        
                swl.append(str(swname))
            messages.add_message(request, messages.INFO, 'Switch-list: ' + str(swl))
            srv = form.cleaned_data['serverselect_in'].name
            prn = form.cleaned_data['prjname_in']
            # Do something with the text (e.g., save to database)

            messages.add_message(request, messages.INFO, 'GNS3 server: ' + str(srv))
            result_out = str(dcnodatg.p_to_v(username=unm, passwd=pwd , servername=srv, switchlist=swl, prjname=prn))
            messages.add_message(request, messages.SUCCESS, 'Project Created: ' + str(prn) + ' on ' + str(srv))
            messages.add_message(request, messages.INFO, 'Open project here: <a href='+result_out+' >'+result_out+'</a>' , extra_tags='safe')
            return render(request, 'golab.html', {'form': form})
    else:
        form = forms.golabForm()
        return render(request, 'golab.html', {'form': form})

class gns3srvView(generic.ObjectView):
    queryset = models.gns3srv.objects.all()
class gns3srvListView(generic.ObjectListView):
    queryset = models.gns3srv.objects.all()
    table = tables.gns3srvTable
class gns3srvEditView(generic.ObjectEditView):
    queryset = models.gns3srv.objects.all()
    form = forms.gns3srvForm
class gns3srvDeleteView(generic.ObjectDeleteView):
    queryset = models.gns3srv.objects.all()


class ptovjobView(generic.ObjectView):
    queryset = models.ptovjob.objects.all()
class ptovjobListView(generic.ObjectListView):
    queryset = models.ptovjob.objects.all()
    table = tables.ptovjobTable
class ptovjobEditView(generic.ObjectEditView):
    queryset = models.ptovjob.objects.all()
    form = forms.ptovjobForm
class ptovjobDeleteView(generic.ObjectDeleteView):
    queryset = models.ptovjob.objects.all()


class switchtojobView(generic.ObjectView):
    queryset = models.switchtojob.objects.all()
class switchtojobListView(generic.ObjectListView):
    queryset = models.switchtojob.objects.all()
    table = tables.switchtojobTable
class switchtojobEditView(generic.ObjectEditView):
    queryset = models.switchtojob.objects.all()
    form = forms.switchtojobForm
class switchtojobDeleteView(generic.ObjectDeleteView):
    queryset = models.switchtojob.objects.all()

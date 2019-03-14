from django.shortcuts import render
from para.models import Client
from para.models import Network_object
import natlas.natlas.natlas
from para.net_discover import discover
from django.http import HttpResponseRedirect
from django.urls import reverse
import _thread

def page(request,pk):
    if request.POST:


        print ("Running Discovery from Web")
        _thread.start_new_thread(discover,(pk,))
        #discover(pk)
        return render(request, 'discover.html', {'pk': pk})
    else:
        print("display")
        return render(request, 'discover.html', {'pk': pk})
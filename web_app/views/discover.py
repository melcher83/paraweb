from django.shortcuts import render
from para.models import Client
from para.models import Network_object
import natlas.natlas.natlas
from para.net_discover import discover
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
import _thread

def page(request,pk):
    if request.POST:



        _thread.start_new_thread(discover,(pk))
        return render(request, 'discover.html', {'pk': pk})
    else:
        return render(request, 'discover.html', {'pk': pk})
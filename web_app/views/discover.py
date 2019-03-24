from django.shortcuts import render
from para.net_discover import discover
from django.http import HttpResponseRedirect
from django.urls import reverse
import sys
import _thread
import logging

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')

def page(request,pk):
    #sys.stdout.flush()
    if request.POST:
        logging.debug("Running Discovery from Web")
        _thread.start_new_thread(discover,(pk,))
        return HttpResponseRedirect(reverse('index'))
    else:
        print("display")
        return render(request, 'discover.html', {'pk': pk})
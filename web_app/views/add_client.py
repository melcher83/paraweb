import natlas.natlas.natlas
from django.shortcuts import render

def page(request):
    return render(request, 'add-client.html', {'action': "Select an Action", })

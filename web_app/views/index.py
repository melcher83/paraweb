from para.models import Client
from django.shortcuts import render
def page(request):
  print("test")
  allclients = Client.objects.all()
  return render(request, 'index.html', {'allclients': allclients })
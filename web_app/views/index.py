#from web.models import Project
from django.shortcuts import render
def page(request):
  #all_projects = Project.objects.all()
  return render(request, 'index.html', {'action': "Select an Action", })
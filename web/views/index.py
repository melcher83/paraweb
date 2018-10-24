from ncart_app.models import Project
from django.shortcuts import render
def page(request):
  all_projects = Project.objects.all()
  return render(request, 'index.html', {'action': "Select an Action", 'all_projects': all_projects})
import natlas.natlas.natlas
from django.shortcuts import render
from para.models import Client
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

def page(request):
  if request.POST:

    form = Form_client(request.POST)
    if form.is_valid():

      form.save()

      # If the form is valid, we store the data in a model record in the form.
      return HttpResponseRedirect(reverse('index'))
      # This line is used to redirect to the specified URL. We use the reverse() function to get the URL from its name defines urls.py.
    else:

      return render(request, 'add_client.html', {'form': form})
  else:

    form = Form_client()
    return render(request, 'add_client.html', {'form': form})
class Form_client(forms.ModelForm):
    class Meta:
        # We extend the Meta class of the ModelForm. It is this class that will allow us to define the properties of ModelForm.
        model = Client
        # We define the model that should be based on the form.
        exclude = ('date_created', 'last_connexion',)

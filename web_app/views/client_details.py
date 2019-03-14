

#  return render(request, 'en/public/project_details_update_form.html', {'project' : project,'project_dict' : project_dict})
from django.shortcuts import render
from para.models import Client
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
def page(request,pk):
  if request.POST:
    instance = Client.objects.get(id=pk) #updates the model
    form = Form_client(request.POST or None, instance=instance)  #updates the model
    if form.is_valid():

      form.save()    #updates the model

      # If the form is valid, we store the data in a model record in the form.
      return HttpResponseRedirect(reverse('index'))
      # This line is used to redirect to the specified URL. We use the reverse() function to get the URL from its name defines urls.py.
    else:

      return render(request, 'client_details.html', {'form' : form})
  else:
    print ("details")
    form1 = Client.objects.get(id=pk)
    form=Form_client(instance=form1)




    return render(request, 'client_details.html', {'form': form, 'pk': pk})
class Form_client(forms.ModelForm):


# Here we create a class that inherits from ModelForm.


  class Meta:
  # We extend the Meta class of the ModelForm. It is this class that will allow us to define the properties of ModelForm.
    model = Client

    # We define the model that should be based on the form.
    exclude = ('date_created', 'last_connexion', )
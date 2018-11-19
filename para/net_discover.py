import natlas.natlas.natlas
from para.models import Client
from para.models import Network_object



class discover:
    def __init__(self, pk):
        form1 = Client.objects.get(id=pk) #get client onject
        natlas_obj = natlas.natlas.natlas() #create natlas object

        config = "web_app/templates/natlas.conf"

        natlas_obj.config_load(config) #load config

        natlas_obj.set_discover_maxdepth(100) # set discovery depth

        natlas_obj.snmp_add_credential(2, form1.snmp_com) #add snmp credentials

        natlas_obj.discover_network(form1.rootip, 1) #discover network
        nodes=natlas_obj.get_discovered_nodes()
        x=0
        for n in nodes:
            obj[x]=Network_object()
            obj[x]= n.serial
            print(obj[x].serial)
            x = x+1



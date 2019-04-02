import natlas.natlas.natlas
from para.models import Client
from para.models import Network_object
from django import forms

import logging

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')

class discover:
    def __init__(self, pk):
        logging.debug ("start")
        form1 = Client.objects.get(id=pk) #get client onject
        natlas_obj = natlas.natlas.natlas() #create natlas object

        config = "web_app/templates/natlas.conf"

        natlas_obj.config_load(config) #load config

        natlas_obj.set_discover_maxdepth(100) # set discovery depth

        #natlas_obj.snmp_add_credential(2, form1.snmp_com) #add snmp credentials
        logging.debug ("discovering network" + " " + form1.rootip)
        natlas_obj.discover_network(form1.rootip, 1) #discover network

        nodes=[]
        logging.debug("getting nodes")
        nodes=natlas_obj.get_discovered_nodes()
        logging.debug("hrlp")
        x=0

        logging.debug ("entering Loop")
        for n in nodes:
            #logging.debug(x)
            obj=Network_object()
            #logging.debug(nodes[n].serial)
            obj.name= n.name
            obj.client_id = pk
            obj.serial=n.serial
            obj.ip = n.ip
            obj.plat = n.plat

            logging.debug("object.client" + " " + obj.client_id)
            logging.debug(obj.serial)
            #x = x+1
            obj.save()

        logging.debug("Loop Complete")





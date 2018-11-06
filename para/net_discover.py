import natlas.natlas.natlas
from para.models import Client
import _thread

class discover:
    def __init__(self, pk):
        form1 = Client.objects.get(id=pk)
        natlas_obj = natlas.natlas.natlas()

        config = "web_app/templates/natlas.conf"
        form1 = Client.objects.get(id=pk)

        natlas_obj.config_load(config)

        natlas_obj.set_discover_maxdepth(10)

        natlas_obj.snmp_add_credential(2, form1.snmp_com)

        natlas_obj.discover_network(form1.rootip, 1))
import natlas.natlas.natlas
snmp_ver=2
snmp_community="cbtm0n"

natlas_obj = natlas.natlas.natlas()

config="natlas.conf"




natlas_obj.snmp_add_credential(snmp_ver, snmp_community)
print(config)
natlas_obj.config_load(config)



natlas_obj.discover_network("10.200.8.1", 1)

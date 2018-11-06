import natlas.natlas.natlas
snmp_ver=2
snmp_community="cBtn3tM0n"

natlas_obj = natlas.natlas.natlas()

config="natlas.conf"





print(config)
natlas_obj.config_load(config)

natlas_obj.set_discover_maxdepth(10)

natlas_obj.snmp_add_credential(snmp_ver, snmp_community)



natlas_obj.discover_network("10.10.96.1", 1)

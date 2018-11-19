from django.db import models

# Create your models here.
class Client(models.Model):
    #Title = models.CharField(verbose_name='Title', max_length=30,null=True, default=None, blank=True)
    client = models.CharField(verbose_name='Client', max_length=30)
    streetaddress = models.CharField(verbose_name='Street Address', max_length=300)
    city = models.CharField(verbose_name='City', max_length=30)
    state = models.CharField(verbose_name='State', max_length=30)
    date = models.DateField(verbose_name='Date Performed')
    zip = models.CharField(verbose_name='Zip Code', max_length=5)
    date_end = models.DateField(verbose_name='Date Ended',null=True, default=None, blank=True)
    contact = models.CharField(verbose_name='Contact', max_length=100)
    email = models.EmailField(verbose_name='Email',null=True, default=None)
    rootip = models.CharField(verbose_name='IP ROOT', null=True, default=None,max_length=300)
    snmp_com = models.CharField(verbose_name='SNMPv2 Community', null=True, default=None, max_length=300)

    def __unicode__(self):
        return self.client

class Network_object(models.Model):
    name = models.CharField(verbose_name='Firewall/Router/Switch Name', max_length=100)
    ip = models.CharField(verbose_name='IP Address',max_length=30,null=True, default=None, blank=True)
    plat = models.CharField(verbose_name='Platform', max_length=30,null=True, default=None, blank=True)
    ios = models.CharField(verbose_name='IOS', max_length=1000, null=True, default=None, blank=True)
    router = models.CharField(verbose_name='Router', max_length=1000, null=True, default=None, blank=True)
    ospf_id = models.CharField(verbose_name='OSPF ID', max_length=1000, null=True, default=None, blank=True)
    bgp_las = models.CharField(verbose_name='BGP LAS', max_length=1000, null=True, default=None, blank=True)
    hsrp_vip = models.CharField(verbose_name='HSRP VIP', max_length=1000, null=True, default=None, blank=True)
    serial = models.CharField(verbose_name='Serial', max_length=1000, null=True, default=None, blank=True)
    bootfile = models.CharField(verbose_name='Bootfile', max_length=1000, null=True, default=None, blank=True)
    svis = models.CharField(verbose_name='SVIS', max_length=1000, null=True, default=None, blank=True)
    links = models.CharField(verbose_name='Links', max_length=1000, null=True, default=None, blank=True)


    #analysis = models.CharField(verbose_name='Analysis', max_length=10000, null=True, default=None, blank=True)
    client = models.ForeignKey(Client, verbose_name="Client", null=True, default=None, blank=True,on_delete = models.CASCADE)



    def __unicode__(self):
        return self.name

class SSH_credentials(models.Model):
    Network_object = models.ForeignKey(Network_object, verbose_name="Network_object", null=True, default=None, blank=True,on_delete = models.CASCADE)
    username=models.CharField(verbose_name='username',max_length=30)
    password=models.CharField(verbose_name='Password', max_length=300)  #need to figure a way out to secure this but also be able to pull it up when needed



    def __unicode__(self):
        return self.username

class SNMPv3_credentials(models.Model):
    Network_object = models.ForeignKey(Network_object, verbose_name="Network_object", null=True, default=None, blank=True,on_delete = models.CASCADE)
    username=models.CharField(verbose_name='username',max_length=30)
    auth=models.CharField(verbose_name='Auth Password', max_length=300)  #need to figure a way out to secure this but also be able to pull it up when needed
    auth_alg = models.CharField(verbose_name='Auth Algorithm', max_length=300) #needs to be a drop down
    priv = models.CharField(verbose_name='Priv Password',max_length=300)  # need to figure a way out to secure this but also be able to pull it up when needed
    auth_alg = models.CharField(verbose_name='Priv Algorithm', max_length=300) #needs to be a drop down



    def __unicode__(self):
        return self.username




# http://docs.openstack.org/developer/python-novaclient/ref/v2/servers.html
import time, os, sys, random, re
import inspect
from os import environ as env

from  novaclient import client
import keystoneclient.v3.client as ksclient
from keystoneauth1 import loading
from keystoneauth1 import session


flavor = ["ssc.large","ssc.large.highmem", "ssc.medium",]
private_net = "UPPMAX 2022/1-1 Internal IPv4 Network"
floating_ip_pool_name = None
floating_ip = None
image_name = "Ubuntu 20.04 - 2021.03.23"

identifier = 2

loader = loading.get_plugin_loader('password')

auth = loader.load_from_options(auth_url=env['OS_AUTH_URL'],
                                username=env['OS_USERNAME'],
                                password=env['OS_PASSWORD'],
                                project_name=env['OS_PROJECT_NAME'],
                                project_domain_id=env['OS_PROJECT_DOMAIN_ID'],
                                #project_id=env['OS_PROJECT_ID'],
                                user_domain_name=env['OS_USER_DOMAIN_NAME'])

sess = session.Session(auth=auth)
nova = client.Client('2.1', session=sess)
print ("user authorization completed.")

image = nova.glance.find_image(image_name)

flavors = [nova.flavors.find(name=flavor[0]), nova.flavors.find(name=flavor[1]), nova.flavors.find(name=flavor[2])]

if private_net != None:
    net = nova.neutron.find_network(private_net)
    nics = [{'net-id': net.id}]
else:
    sys.exit("private-net not defined.")

#print("Path at terminal when executing this file")
#print(os.getcwd() + "\n")
cfg_file_path =  os.getcwd()+'/cloud-cfg.txt'
if os.path.isfile(cfg_file_path):
    userdata_base = open(cfg_file_path)
else:
    sys.exit("prod-cloud-cfg.txt is not in current working directory")

cfg_file_path =  os.getcwd()+'/cloud-cfg.txt'
if os.path.isfile(cfg_file_path):
    userdata_combiner = open(cfg_file_path)
else:
    sys.exit("dev-cloud-cfg.txt is not in current working directory")    

cfg_file_path =  os.getcwd()+'/cloud-cfg.txt'
if os.path.isfile(cfg_file_path):
    userdata_client = open(cfg_file_path)
else:
    sys.exit("dev-cloud-cfg.txt is not in current working directory")    


secgroups = ['default','derek_c3_2']

print ("Creating instances ... ")
instance_base = nova.servers.create(name="derek_c3_2_base"+str(identifier), image=image, flavor=flavors[0], key_name='derekmacair2',userdata=userdata_base, nics=nics,security_groups=secgroups)
instance_combiner = nova.servers.create(name="derek_c3_2_combiner"+str(identifier), image=image, flavor=flavors[1], key_name='derekmacair2',userdata=userdata_combiner, nics=nics,security_groups=secgroups)
instance_client = nova.servers.create(name="derek_c3_2_client"+str(identifier), image=image, flavor=flavors[2], key_name='derekmacair2',userdata=userdata_client, nics=nics,security_groups=secgroups)
inst_status_base = instance_base.status
inst_status_combiner = instance_combiner.status
inst_status_client = instance_client.status


print ("waiting for 10 seconds.. ")
time.sleep(10)

while inst_status_base == 'BUILD' or inst_status_combiner == 'BUILD' or inst_status_client == 'BUILD':
    print ("Instance: "+instance_base.name+" is in "+inst_status_base+" state, sleeping for 5 seconds more...")
    print ("Instance: "+instance_combiner.name+" is in "+inst_status_combiner+" state, sleeping for 5 seconds more...")
    print ("Instance: "+instance_client.name+" is in "+inst_status_client+" state, sleeping for 5 seconds more...")
    time.sleep(5)
    instance_base = nova.servers.get(instance_base.id)
    inst_status_base = instance_base.status
    instance_combiner = nova.servers.get(instance_combiner.id)
    inst_status_combiner = instance_combiner.status
    instance_client = nova.servers.get(instance_client.id)
    inst_status_client = instance_client.status

ip_address_prod = None
for network in instance_base.networks[private_net]:
    if re.match('\d+\.\d+\.\d+\.\d+', network):
        ip_address_prod = network
        break
if ip_address_prod is None:
    raise RuntimeError('No IP address assigned!')

ip_address_dev = None
for network in instance_combiner.networks[private_net]:
    if re.match('\d+\.\d+\.\d+\.\d+', network):
        ip_address_dev = network
        break
if ip_address_dev is None:
    raise RuntimeError('No IP address assigned!')

ip_address_client = None
for network in instance_client.networks[private_net]:
    if re.match('\d+\.\d+\.\d+\.\d+', network):
        ip_address_client = network
        break
if ip_address_client is None:
    raise RuntimeError('No IP address assigned!')

print ("Instance: "+ instance_base.name +" is in " + inst_status_base + " state" + " ip address: "+ ip_address_prod)
print ("Instance: "+ instance_combiner.name +" is in " + inst_status_combiner + " state" + " ip address: "+ ip_address_dev)
print ("Instance: "+ instance_client.name +" is in " + inst_status_client + " state" + " ip address: "+ ip_address_client)

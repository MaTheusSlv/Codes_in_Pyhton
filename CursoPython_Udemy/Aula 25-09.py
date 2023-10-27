#CISCO - Netmiko

# O Netmiko é uma biblioteca Python para simplificar o SSH para gerenciar dispositivos de rede
# Para usar o Netmiko, deve-se estar habilitado o SSH nos dispositivos
# Precisa-se baixar a biblioteca da Netmiko para utilizá-la
# Utilizando o Netmiko:

from netmiko import ConnectHandler

R1 = {
'device_type':'cisco_ios',
'host':'192.168.0.101',
'username':'admin',
'password':'password'
}

connect = ConnectHandler(**R1)
output = connect.send_command('show ip int brief')

print(output)


#CISCO - Netmiko CONFIG PARA CRIAR UM LOOPBACK INTERFACE

from netmiko import ConnectHandler

R1 = {
'device_type':'cisco_ios',
'host':'192.168.0.101',
'username':'admin',
'password':'password'
}

connect = ConnectHandler(**R1)

loopback13 = ['interface loopback 13']

configurar = connect.send_config_set(loopback13)
output = connect.send_command('show ip int brief')

print(output)


#CISCO - Netmiko PARA ACESSAR MULTIPLOS DISPOSITIVOS

from netmiko import ConnectHandler

R1 = {
'device_type':'cisco_ios',
'host':'192.168.0.101',
'username':'admin',
'password':'password'
}

R2 = {
'device_type':'cisco_ios',
'host':'192.168.0.102',
'username':'admin',
'password':'password'
}

R3 = {
'device_type':'cisco_ios',
'host':'192.168.0.103',
'username':'admin',
'password':'password'
}

for routers in (R1, R2, R3):
    connect = ConnectHandler(**routers)
    print(connect.find_prompt())
    connect.disconnect()

print('Script finalizado!')


#CISCO - Netmiko File

# Criar um arquivo de configuração 'config-router-file'
    #clock timezone EST -4
    #ntp server 1.1.1.1
    #logging console 7
    #username marcos privilege 15 secret cisco
    #username paulo privilege 15 secret cisco
    #snmp-server community public ro
    #interface loopback 10

from netmiko import ConnectHandler

R1 = {
'device_type':'cisco_ios',
'host':'192.168.0.101',
'username':'admin',
'password':'password'
}

R2 = {
'device_type':'cisco_ios',
'host':'192.168.0.102',
'username':'admin',
'password':'password'
}

R3 = {
'device_type':'cisco_ios',
'host':'192.168.0.103',
'username':'admin',
'password':'password'
}

with open('config-router-file') as file:
    config_line = file.read().splitlines()

lista_routers = [R1, R2, R3]

for routers in lista_routers:
    connect = ConnectHandler(**routers)
    configure = connect.send_config_set(config_line)
    print(configure)
    connect.disconnect()

print('Script finalizado!')


#CISCO - Napalm

# Napalm é uma biblioteca Python que se conecta via SSH com dispositivos de rede
# Precisa-se baixar a biblioteca da Netmiko para utilizá-la
# Utilizando o Napalm:

from napalm import get_network_driver
import json

driver = get_network_driver("ios")

device = driver(
        hostname="127.0.0.1",
        username="vagrant",
        password="vagrant",
        optional_args={"port": 12443},
    )

device.open()

output = device.get_facts
print(json.dumps(output, indent=4))


#CISCO - Napalm com BGP

# Criar um arquivo de configuração 'r1-config.cfg'
    #ip scp server enable
    #inter g0/1
    #ip address 10.100.102.1 255.255.2555.0
    #no shutdown
    #interface loopback 0
    #ip address 1.1.1.1 255.255.255.0
    #router bgp 200
    #neighbor 10.100.102.2 remote-as 300
    #network 1.1.1.0 mask 255.255.255.0

# Criar um arquivo de configuração 'r2-config.cfg'
    #ip scp server enable
    #inter g0/1
    #ip address 10.100.102.2 255.255.2555.0
    #no shutdown
    #interface loopback 0
    #ip address 2.2.2.2 255.255.255.0
    #router bgp 300
    #neighbor 10.100.102.1 remote-as 200
    #network 2.2.2.0 mask 255.255.255.0

# Utilizando o Napalm:

from napalm import get_network_driver
import json

driver = get_network_driver("ios")

device = driver(
        hostname="127.0.0.1",
        username="vagrant",
        password="vagrant",
        optional_args={"port": 12443},
    )

device.open()
print('Configurando o router... Aguarde...')

device.load_merge_candidate(filename='r1-config.cfg')
device.commit_config()
device.close()

print('Configuração finalizada com sucesso!')
# CISCO - AUTOMAÇÃO PYTHON

# Com a topologia configurada para ter acesso a rede, configurar os dispositivos para utilizarem o TELNET
# Baixar a biblioteca Telnetlib que permitirá usar o TELNET para controlar os dispositivos

# Criar um arquivo .py para criar uma interface loopback:

import getpass
import telnetlib

HOST = "localhost" #Endereço de onde vc quer fazer o TELNET
user = input("Digite o seu usuário: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"login: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")
#Fazendo os comandos do aparelho
tn.write(b"conf t\n")
tn.write(b"interface loopback 0\n")
tn.write(b"ip address 1.1.1.1 255.255.255.0\n")
tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))


# Criar um arquivo .py para criar Vlans:

import getpass
import telnetlib

HOST = "localhost" #Endereço de onde vc quer fazer o TELNET
user = input("Digite o seu usuário: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"login: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")
#Fazendo os comandos do aparelho
tn.write(b"conf t\n")
tn.write(b"vlan 2\n")
tn.write(b"name Sales")
tn.write(b"vlan 3\n")
tn.write(b"name Eng")
tn.write(b"vlan 4\n")
tn.write(b"name Prod")
tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))


# Criar um arquivo .py para habilitar o OSPF:

import getpass
import telnetlib

HOST = "localhost" #Endereço de onde vc quer fazer o TELNET
user = input("Digite o seu usuário: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"login: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")
#Fazendo os comandos do aparelho
tn.write(b"conf t\n")
tn.write(b"interface gi0/1\n")
tn.write(b"ip add 10.100.102.1 255.255.255.252\n")
tn.write(b"no shutdown\n")
tn.write(b"router ospf 1\n")
tn.write(b"network 10.100.102.0 0.0.0.3 area 0\n")
tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))


# Criar um arquivo .py para criar Vlans com loop:

import getpass
import telnetlib

HOST = "localhost" #Endereço de onde vc quer fazer o TELNET
user = input("Digite o seu usuário: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"login: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")
#Fazendo os comandos do aparelho
tn.write(b"conf t\n")

for vlans in range(10,15):
    tn.write(b"Vlan " + str(vlans).encode('ascii') + b"\n")
    tn.write(b"name Site_" + str(vlans).encode('ascii') + b"\n")

tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))


# Criar um arquivo .py para criar interfaces loopback em vários aparelhos:

        # Criar arquivo (routers-ip) com endereços de IP dos roteadores
            # 192.168.0.101
            # 192.168.0.102
            # 192.168.0.103

import getpass
import telnetlib

HOST = "localhost" #Endereço de onde vc quer fazer o TELNET
user = input("Digite o seu usuário: ")
password = getpass.getpass()

lista_routers = open('routers-ip')

for ip in lista_routers:
    ip=ip.strip()
    print('Estamos configurando o roteador' + (ip))
    HOST = ip
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"login: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")
#Fazendo os comandos do aparelho
    tn.write(b"conf t\n")
    for interface_loopback in range(1,4):
        tn.write(b"interface loopback" + str(interface_loopback).encode('ascii') + b"\n")
    tn.write(b"end\n")
    tn.write(b"exit\n")

    print(tn.read_all().decode('ascii'))

print('Configuração completa!')


# Criar um arquivo .py para realizar backup de configurações:

import getpass
import telnetlib

user = input("Digite o seu usuário: ")
password = getpass.getpass()

lista_routers = open('routers-ip')

for ip in lista_routers:
    ip=ip.strip()
    print('Realizando o backup do roteador' + (ip))
    HOST = ip
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"login: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")
#Fazendo os comandos do aparelho
    tn.write(b"terminal length 0\n")
    tn.write(b"show run\n")
    tn.write(b"exit\n")

    ler_config = tn.read_all()
    save_config = open('backup-' + HOST, 'w')
    save_config.write(ler_config.decode('ascii'))
    save_config.write('\n')
    save_config.close()


print('Backup completo!')
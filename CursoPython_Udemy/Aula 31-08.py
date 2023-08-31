#ADICIONANDO MAIS FUNÇÕES A CLASSE
'''
class Funcionarios:
    def __init__(self, nome, sobrenome, data_nascimento):
        self.nome= nome
        self.sobrenome= sobrenome
        self.data_nascimento= data_nascimento
    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome

usuario1 = Funcionarios('Elena', 'Cabral', '12/01/2009')
usuario2 = Funcionarios('Carol', 'Silva', '15/10/2005')
usuario3 = Funcionarios('André', 'Iacono', '11/03/2003')

print(usuario1.nome + ' ' + usuario1.sobrenome)
print(usuario1.nome_completo())
'''

#CALCULANDO A IDADE DO FUNCIONÁRIO
'''
from datetime import datetime

class Funcionarios:
    def __init__(self, nome, sobrenome, ano_nascimento):
        self.nome= nome
        self.sobrenome= sobrenome
        self.ano_nascimento= ano_nascimento
    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome
    def idade_funcionario(self):
        ano_atual = datetime.now().year
        self.ano_nascimento = int(ano_atual - self.ano_nascimento)
        return self.ano_nascimento

usuario1 = Funcionarios('Elena', 'Cabral', 2009)
usuario2 = Funcionarios('Carol', 'Silva', 2005)
usuario3 = Funcionarios('André', 'Iacono', 2003)

print(Funcionarios.idade_funcionario(usuario1))
'''

#MÓDULOS
'''
#MÓDULOS SÃO OS ARQUIVOS QUE PODEM GUARDAR FUNÇÕES

## funcoes.py

def somer():
    print('Esta função vai somar valores')

def multi():
    print('Esta função vai multiplicar valores')

## main.py

import funcoes  #O IMPORT TRAZ TODAS AS FUNÇÕES DO ARQUIVO, CONSOME MAIS MEMÓRIA
from funcoes import somar  #O FROM ESPECIFICA QUAL FUNÇÃO IMPORTAR E PERMITE EXECUTÁ-LA SEM USAR O "funcoes." ANTES

funcoes.somar()

somar()
'''

#CRIANDO E IMPORTANDO PACKAGES
'''
## items/cadastro.py

def cliente():
    print('Cadastro do cliente')

## items/calculo.py


## items/__init__.py #ESSE ARQUIVO VAZIO INDICA AO PYTHON QUE AQUELA PASTA É UM PACKAGE

## funcoes.py

def somer():
    print('Esta função vai somar valores')

def multi():
    print('Esta função vai multiplicar valores')

## main.py

from funcoes import somar
from funcoes import multi
from items.cadastro import cliente

somar()
multi()
cliente()
'''

#APLICANDO MÓDULOS
'''
## main.py

from funcoes import find_index

list1=['a','b','c','d','e']

var1 = find_index(list1, 'b')
print(var1)

## funcoes.py

def find_index(to_find, item):
    for i, valor in enumerate(to_find):
        if valor == item:
            return i
    return -1
'''

#DESAFIO PONTO DO STEAK(IF ELSE)
'''
temperatura = int(input('Qual é a temperatura da carne? '))

if temperatura < 48:
    print('Cozinhar por mais alguns minutos')
elif temperatura >= 48 and < 54:
    print('Selada')
elif temperatura >= 54 and < 60:
    print('Ao ponto para o mal')
elif temperatura >= 60 and < 65:
    print('Ao ponto')
elif temperatura >= 65 and < 70:
    print('Ao ponto para o bem')
else:
    print('Bem passada')

## OUTRA FORMA

temperatura = int(input('Qual é a temperatura da carne? '))

if temperatura < 48:
    print('Cozinhar por mais alguns minutos')
elif temperatura in range(48, 53):
    print('Selada')
elif temperatura in range(54, 59):
    print('Ao ponto para o mal')
elif temperatura in range(60, 64):
    print('Ao ponto')
elif temperatura in range(65, 70):
    print('Ao ponto para o bem')
else temperatura >= 71:
    print('Bem passada')
'''
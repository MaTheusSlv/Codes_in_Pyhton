#DICIONÁRIOS
'''
#Utilizam index no formato de Keys e Values

aluno={'nome': 'Ana', 'idade': 16, 'nota_final':'A', 'aprovação': True}

print(aluno['nome'])
'''

#MANIPULANDO ITENS DO DICIONÁRIOS
'''
aluno={'nome': 'Ana', 'idade': 16, 'nota_final':'A', 'aprovação': True}

aluno['nome']= 'José'
#OU
aluno.update({'nome':'José', 'nota_final':'B'}) #MUDAM OS ITENS DO DICIONÁRIO

aluno.update({'endereço':'Rua A'}) #ADICIONA O "ENDEREÇO" NO FIM DO DICIONÁRIO

print(aluno)
print(aluno.get('endereço', 'Não existe')) #O .GET() PERMITE BUSCAR O VALOR DA KEY E RETORNAR UMA MENSAGEM CASO NÃO EXISTA

del aluno['idade'] #O DEL APAGA A KEY DO DICIONÁRIO
print(aluno)
'''

#LOOPING DENTRO DO DICIONÁRIO
'''
aluno={'nome': 'Ana', 'idade': 16, 'nota_final':'A', 'aprovação': True}

for x in aluno.values():  #O .VALUES() INDICA QUE DEVERÁ TRAZER OS VALORES DAS KEYS
    print(x)

for x in aluno.items():  #O .ITEMS() INDICA QUE DEVERÁ TRAZER AS KEYS E OS VALORES DAS KEYS
    print(x)
#OU ASSIM, IMPRIMINDO ELES FORA DE UMA TUPLE
for keys, values in aluno.items():
    print(keys, values)
'''

#VISUALIZANDO ITENS, KEYS E VALUES
'''
aluno={
    'nome': 'Ana',
    'idade': 16,
    'nota_final':'A',
    'aprovação': True,
    'matérias':['fisica', 'matemática', 'ingles']
    }

print(aluno)
print(aluno.get('matérias'))
print(len(aluno)) #O LEN() TRAZ O NÚMERO DE KEYS DO DICIONÁRIO
print(aluno.keys()) #O .KEYS() TRAZ AS KEYS DO DICIONÁRIO
'''

#FUNÇÃO LAMBDA
'''
#FUNÇÃO PEQUENA SEM NOME, PODE TER VÁRIOS ARGUMENTOS E SOMENTE UMA EXPRESSÃO

def somar(x):
    return x + 10

print(somar(2))

somar10 = lambda x,y: x + y + 10
print(somar10(2, 4))

#LAMBDA PODE SER CONSIDERADA UMA SUB-FUNÇÃO, OU UMA FUNÇÃO QUE SERÁ USADA UMA VEZ SÓ NAQUELA PARTE DO CÓDIGO
'''

#LAMBDA DENTRO DE UMA OUTRA FUNÇÃO
'''
def somar(x):
    func2= lambda x: x + 10
    return func2(x) * 4

print(somar(2))
'''

#FUNÇÃO MAP DENTRO DE UMA LISTA
'''
#MAPEIA UMA FUNÇÃO À UMA LISTA, MAPEIA UMA FUNÇÃO A UM ITERABLE

lista1=[1, 2, 3, 4]

def multi(x):
    return x * 2

print(multi(2))

lista2=map(multi, lista1)

print(list(lista2))
'''

#FUNÇÃO MAP COM O LAMBDA
'''
lista1=[1, 2, 3, 4]

print(list(map(lambda x: x * 2, lista1)))
'''

#FUNÇÃO FILTER
'''
valores=[10, 12, 34, 44, 57]

def remover20(x):
    return x > 20

print(list(filter(remover20, valores)))

#OU

print(list(filter(lambda x: x > 20, valores)))
'''

#LIST COMPREHENSION COM STRINGS
'''
#BEM MAIS SIMPLES DE SE ESCREVER, CRIAR UMA NOVA LISTA A PARTIR DE UMA EXISTENTE
#[expressao for item in item]

frutas1=['abacate', 'banana', 'morango', 'kiwi', 'abacaxi']
frutas2=[]

for item in frutas1:
    if 'b' in item:
        frutas2.append(item)

print(frutas2)

#EM UMA LINHA

frutas2=[item for item in frutas1 if 'b' in item]

print(frutas2)
'''

#LIST COMPREHENSION COM NÚMEROS
'''
valores=[]

for x in range(6):
    valores.append(x * 10)

print(valores)

#EM UMA LINHA

valores=[x * 10 for x in range(6)]

print(valores)
'''

#LISTAS E GENERATOR EXPRESSIONS
'''
#MENOS MEMÓRIA ALOCADA, VALORES EM BYTES

from sys import getsizeof

numeros= [ x * 10 for x in range(1000) ]
print(type(numeros))
print(numeros)
print(getsizeof(numeros)) #O GETSIZEOF() TRAZ O QUANTO QUE AQUELA LISTA USA DA MEMÓRIA

numeros= ( x * 10 for x in range(1000) )
print(type(numeros))
print(list(numeros))
print(getsizeof(numeros)) #O GENERATOR EXPRESSION USA MENOS MEMÓRIA QUE UMA LISTA
'''
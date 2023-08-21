#FUNCTIONS AND LIBRARIES
'''
Functions(Maçã)= Códigos que podem ser reutilizados em todo o código, quando chamados trazem seus atributos definidos

Module(Sessão de frutas)= Um conjunto de Functions que podem ser usadas

Package(Supermercado)= Um conjunto de Modules

Librarie(Rede)= Um conjunto de packages
'''

#FUNCIONAMENTO DA FUNCTION
'''
#DRY = Don't Repeat Yourself
#Funções são usadas para não se repetir códigos

def boas_vindas():
    print('Olá Marcos!')
    print('Temos 5 laptops em estoque')

boas_vindas()
'''

#FUNÇÃO DE SOMA
'''
def somar_dois_numeros():
    numero1=10
    numero2=5
    resultado= numero1 + numero2
    print(resultado)

somar_dois_numeros()

#VARIÁVEIS GLOBAIS SÃO AS QUE ESTÃO FORA DE FUNÇÕES
'''

#PARÂMETROS E ARGUMENTOS DE FUNÇÕES
'''

def boas_vindas(nome, quantidade): #NOME E QUANTIDADE SÃO PARÂMETROS
    print(f'Olá {nome}.')
    print(f'Temos {str(quantidade)} laptops em estoque')

boas_vindas('Marcos', 5) #'MARCOS' E 5 SÃO OS ARGUMENTOS
boas_vindas('Ronaldo', 4)
boas_vindas('Maria', 2)

######################################## AO INVÉS DE ##############################################################################
def boas_vindas_marcos():
    print('Olá Marcos!')
    print('Temos 5 laptops em estoque')

def boas_vindas_ronaldo():
    print('Olá Ronaldo!')
    print('Temos 4 laptops em estoque')

def boas_vindas_maria():
    print('Olá Maria!')
    print('Temos 2 laptops em estoque')

boas_vindas_marcos()
boas_vindas_ronaldo()
boas_vindas_maria()

'''

#ARGUMENTOS DEFAULT E NÃO DEFAULT
'''
def boas_vindas(nome, quantidade=6): # =6 DEFINE QUE O PARÂMETRO 'QUANTIDADE' SERÁ DEFAULT 6
    print(f'Olá {nome}.')
    print(f'Temos {str(quantidade)} laptops em estoque')

boas_vindas('Marcos', 4) #SE VOCÊ PASSAR UM VALOR PARA UM PARÂMETRO DEFAULT ELE SOBSCREVERÁ

#A ORDEM DOS PARÂMETROS DEVEM SER TAIS QUE OS PARÂMETROS DEFAULT SEMPRE DEVERÃO VIR APÓS OS NÃO DEFAULT
'''

#PRINT OU RETURN EM FUNCTIONS
'''
#'Funções ou retornam um valor ou realizam uma tarefa'
#Realizar(PRINT) // Retornar(DÊ ESSE RESULTADO)

def cliente1(nome):
    print(f'Olá {nome}')

cliente1('Maria')

def cliente2(nome):
    return f'Olá {nome}'

print(cliente2('José'))

#O RETURN GUARDA O VALOR NA MEMÓRIA, O PRINT SÓ IMPRIME E MAIS NADA(NÃO GUARDA NADA)
'''
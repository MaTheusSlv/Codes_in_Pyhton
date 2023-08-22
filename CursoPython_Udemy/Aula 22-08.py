#VÁRIOS ARGUMENTOS "xargs"
'''
#Função que soma vários números

def soma(*numeros): #O '*' indica que podem ser várias entradas para aquele argumento
    resultado = 0
    for num in numeros:
        resultado += num
    return resultado

x=soma(2,3,4,7)

print(x)
'''

#NOMEANDO PARÂMETROS xargs
'''
def agencia(**carro):  #O '**' indica que podem ser usados vários parâmetros
    return carro

print(agencia(marca='Gol', cor='Branca', motor=1.0))
print(agencia(marca='Prisma', cor='Branca', motor=1.4))
print(agencia(marca='Gol', cor='Preto', motor=1.0))
'''

#IMPORTANDO UM MÓDULO
'''
#Qual é o número fatorial de 4?
# 4 * 3 * 2 * 1 = 24

import math #IMPORTANDO UM MÓDULO AO CÓDIGO

print(math.factorial(4)) #UTILIZANDO UM MÓDULO

fatorial = 4*3*2*1
print(fatorial)

'''
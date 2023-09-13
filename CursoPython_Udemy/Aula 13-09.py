#DESAFIO DE SOMA COM FUNÇÕES
'''
def somar():
    num1 = float(input('Digite o 1° Número: '))
    num2 = float(input('Digite o 2° Número: '))
    soma = num1 + num2
    print(f'O {num1} somado ao {num2} é igual a {soma}')

somar()

##  OUTRA FORMA

def soma(num1, num2):
    return num1+num2

user_num1=int(input('Digite o 1° Número: '))
user_num2=int(input('Digite o 2° Número: '))

print(soma(user_num1, user_num2))
'''

#DESAFIO DE CALCULAR BASE E EXPOENTES
'''
def exponenciacao(base, expoente=2):
    return base ** expoente

base = float(input('Digite o número base: '))
expoente = input('Digite o número expoente: ')

if expoente:
    print(exponenciacao(base, int(expoente)))
else:
    print(exponenciacao(base))

##  OUTRA FORMA

def potencia(base, expoente=2):
    return base ** expoente

base = float(input('Digite o número base: '))
expoente = input('Digite o número expoente: ')

if expoente:
    print(potencia(base, int(expoente)))
else:
    print(potencia(base))
'''

#DESAFIO CALCULANDO FATORIAL
'''
def fatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * fatorial(numero - 1)
    
numero = int(input('Digite um número: '))

print(f'O fatorial é {fatorial(numero)}')

##  OUTRA FORMA

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)
    
user_number = int(input('Digite um número: '))

print(f'O fatorial de {user_number} é {fatorial(user_number)}')
'''
#DESAFIO DAS DUAS FUNÇÕES
'''
def dobro(num):
    return num * 2

def quadrado(num):
    return dobro(num) ** 2

num = int(input('Digite um número para o calculo: '))

print(f'O quadrado do dobro do número {num} é {quadrado(num)} !')

##  OUTRA FORMA

def dobrar(num):
    return num*2

def quadrado(num):
    return dobrar(num)**2

user_number=int(input('Digite um número: '))

print(f'O quadrado do dobro do número {user_number} é {quadrado(num)}')
'''

#DESAFIO CONVERTENDO PARA LAMBDA
'''
num = int(input('Digite um número: '))
cubo = lambda num: num ** 3

print(f'O cubo do número {num} é {cubo(num)}!')

##  OUTRA FORMA

cubo=lambda num:num**3

user_number=int(input('Digite um número: '))
print(f'O cubo de {user_number} é {cubo(user_number)}')
'''

#DESAFIO MULTIPLICANDO COM LAMBDA
'''
multiplicacao = lambda num1, num2 : num1 * num2

num1 = float(input('Digite o 1° número: '))
num2 = float(input('Digite o 2° número: '))

print(f'{num1} multiplicado por {num2} é {multiplicacao(num1, num2)}')

## OUTRA FORMA

multiplicar=lambda num1,num2:num1*num2

user_number1=float(input('Digite o 1° número: '))
user_number2=float(input('Digite o 2° número: '))

print(f'A multiplicação de {user_number1} e {user_number2} é {multiplicar(user_number1,user_number2)}')
'''
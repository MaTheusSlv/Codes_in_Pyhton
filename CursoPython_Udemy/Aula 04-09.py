#DESAFIO CALCULO DE IMC
'''
altura = float(input('Qual é a sua Altura em cm: '))
peso = float(input('Qual é o seu peso em kg: '))

def calculo_imc():
    imc = peso / ((altura * altura)/100)

    if imc < 18.5:
        print('MAGREZA')
    elif imc in range(18.5, 24.9):
        print('NORMAL')
    elif imc in range(25.0, 29.9):
        print('SOBREPESO')
    elif imc in range(30.0, 39.9):
        print('OBESIDADE')
    elif imc > 40.0:
        print('OBESIDADE GRAVE')

calculo_imc()

## OUTRA FORMA

altura = float(input('Qual é a sua Altura em cm: '))
peso = float(input('Qual é o seu peso em kg: '))
imc = peso / (altura/100)**2

if imc < 18.5:
    print('magreza')
elif imc >= 18.5 and imc < 24.9:
    print('normal')
elif imc >= 25.0 and imc < 29.9:
    print('sobrepeso')
elif imc >= 30.0 and imc <39.9:
    print('obesidade')
else:
    print('obesidade grave')
'''

#DESAFIO DO PRINT
'''
print('Olá, mundo Python!')

## OUTRA FORMA

print('Olá, mundo Python!')
'''

#DESAFIO DAS VARIÁVEIS
'''
nome = input('Qual o seu nome? ')
idade = int(input('Quantos anos você têm? '))

print(f'Olá, meu nome é {nome} e eu tenho {idade} anos')

## OUTRA FORMA

first_name = input('Qual o seu nome? ')
age = int(input('Qual a sua idade? '))

print('Olá, meu nome é ', first_name, ' e eu tenho ', age, ' anos.')
'''

#DESAFIO DE NÚMEROS
'''
num1 = 10
num2 = 3.5
divisao = num1 / num2

print(divisao)

## OUTRA FORMA

num1=10
num2=3.5
result=num1/num2

print('O resultado da divisão é ', result)
'''

#DESAFIO DO INPUT
'''
nome = input('Qual o seu nome? ')
anos = int(input('Quantos anos você têm? '))

print(f'Olá, {nome}! você têm {anos} anos')

## OUTRA FORMA

first_name=input('Por favor, digite o seu nome: ')
age=int(input('Agora, digite a sua idade: '))

print('Olá, {}! você têm {} anos'.format(first_name, age))
'''
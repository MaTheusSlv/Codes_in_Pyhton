#DESAFIO CONTADOR DE LISTA
'''
frutas = ['Maçã', 'Abacaxi', 'Maçã', 'Mamão', 'Maçã', 'Uva']

maca = 0

for fruta in frutas:
    if fruta == 'Maçã':
        maca = maca + 1

print(f'Números de Maçãs na lista: {maca}')

##  OUTRA FORMA

frutas = ['Maçã', 'Abacaxi', 'Maçã', 'Mamão', 'Maçã', 'Uva']

contador=0

for fruta in frutas:
    if fruta == 'Maçã':
        contador+=1

print('Número de maças na lista: ', contador)
'''

#DESAFIO VERIFICANDO NÚMEROS COM IF ELSE
'''
numero = int(input('Digite um número: '))

if numero > 10:
    print('O número é maior que 10')
elif numero <= 10:
    print('O número é menor ou igual a 10')

##  OUTRA FORMA

numero=int(input('Digite um número: '))

if numero >10:
    print('O número é maior que 10')
else:
    print('O número é menor ou igual a 10')
'''

#DESAFIO DO VERIFICADOR DE IDADE
'''
idade = int(input('Digite a sua idade: '))

if idade < 13:
    print('Você é uma criança')
elif idade >= 13 and idade < 20:
    print('Você é um adolescente')
else:
    print('Você é um adulto')

##  OUTRA FORMA

age=int(input('Digite sua idade: '))

if age <13:
    print('Você é uma criança!')
elif age >=13 and age <20:
    print('Você é um adolescente!')
else:
    print('Você é adulto')
'''

#DESAFIO DE PROCURA EM LISTAS
'''
carro_cli = input('Digite o nome do carro que quer comprar: ')
estoque = ['BMW X6','BMW I5','BMW I8']

if carro_cli in estoque:
    print('Este carro está disponível')
else:
    print('Desculpe, este carro não está disponível')

## OUTRA FORMA

estoque=['BMW X6','BMW I5','BMW I8']
pesquisa_carro=input('Digite o carro desejado: ')

if pesquisa_carro in estoque:
    print('O carro está disponível em estoque')
else:
    print('O carro não está disponível em estoque')
'''
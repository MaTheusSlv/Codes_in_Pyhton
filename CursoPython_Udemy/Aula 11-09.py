#DESAFIO ENCONTRANDO UM ITEM COM WHILE
'''
fruta = input('Digite o nome da fruta: ')

while fruta != 'abacate':
   fruta = input('Digite o nome da fruta: ')
else:
   print('Parabéns, você acertou a fruta!')

##  OUTRA FORMA

while True:
   fruta=input('Digite o nome de uma fruta: ')
   if fruta.lower() == 'abacate':
      break

print('Parabéns, você acertou a fruta')
'''

#DESAFIO PAR E IMPAR
'''
numeros = [1,2,3,4,5,6,7,8,9,10]

for numero in numeros:
    if numero % 2 == 0:
        print(f'O número {numero} é par')
    else:
        print(f'O número {numero} é impar')

##  OUTRA FORMA

numeros=[1,2,3,4,5,6,7,8,9,10]
numeros=list(range(1,11))

for numero in numeros:
    if numero % 2 == 0:
        print(f'O número {numero} é par!')
    else:
        print(f'O número {numero} é impar!')
'''

#DESAFIO LISTA DE CIDADES
'''
cidades = ('São Paulo','Rio de Janeiro','Salvador')
cidade = input('Digite o nome da cidade: ')

if cidade in cidades:
    print('A cidade está na lista de cidades')
else:
    print('A cidade não está na lista de cidades')

##  OUTRA FORMA

cidades = ('São Paulo','Rio de Janeiro','Salvador')
cidade = input('Digite o nome da cidade: ')

if cidade in cidades:
    print('A cidade está na lista de cidades')
else:
    print('A cidade não está na lista de cidades')
'''
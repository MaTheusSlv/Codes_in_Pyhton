#DESAFIO LAMBDA COM IF ELSE
'''
par_ou_impar = lambda numero: 'Par' if numero % 2 ==0 else 'Impar'

numero = int(input('Digite um número: '))

print(par_ou_impar(numero))

##  OUTRA FORMA

par_ou_impar = lambda num: 'Par' if num % 2 ==0 else 'Impar'

num = int(input('Digite um número: '))

print(f'O número {num} é {par_ou_impar(num)}')
'''

#DESAFIO LAMBDA COM FOOR LOOP
'''
numeros = [1,2,3,4,5,6]

quadrado = lambda num: num ** 2

for x in numeros:
    print(f'{quadrado(x)} ', end='')
    
##  OUTRA FORMA

numeros=[1,2,3,4,5,6]
quadrado=lambda num: num**2
resultados=[]

for i in numeros:
    resultados.append(quadrado(i))

print(f'Os quadrados dos números {numeros} são {resultados}')
'''
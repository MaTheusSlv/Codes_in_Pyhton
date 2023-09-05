#DESAFIO DE OPERADORES
'''
num1 = float(input('Digite o 1° Número: '))
num2 = float(input('Digite o 2° Número: '))

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 ** num2)

## OUTRA FORMA

num1=float(input('Digite o primeiro número: '))
num2=float(input('Digite o segundo número: '))

soma=num1+num2
subtracao=num1-num2
multiplicacao=num1*num2
divisao=num1/num2
exponenciacao=num1**num2

print(f'Soma: {soma}')
print(f'Subtração: {subtracao}')
print(f'Multiplicação: {multiplicacao}')
print(f'Divisão: {divisao}')
print(f'Exponenciação: {exponenciacao}')
'''

#DESAFIO DE LISTAS
'''
frutas = ['Maçã', 'Banana', 'Manga', 'Uva']

print(frutas)

## OUTRA FORMA

frutas=['Maçã', 'Banana', 'Manga', 'Uva']

print(frutas)
'''

#DESAFIO DE MODIFICAR LISTAS
'''
frutas = ['Maçã', 'Banana', 'Manga', 'Uva']

print(frutas[0])
print(frutas[-1])

## OUTRA FORMA

frutas=['Maçã', 'Banana', 'Manga', 'Uva']

print(f'A primeira fruta é: {frutas[0]}')
print (f'A últia fruta é: {frutas[-1]}')
'''

#DESAFIO DE INDEX DE LISTAS
'''
frutas = ['Maçã', 'Banana', 'Manga', 'Uva']
frutas[1] = 'Morango'
frutas.append('Abacaxi')

print(frutas)

## OUTRA FORMA

frutas=['Maçã', 'Banana', 'Manga', 'Uva']
frutas[1]='Morango'
frutas.append('Abacaxi')

print(frutas)
'''

#DESAFIO DE REMOVER ITENS DA LISTA
'''
frutas = ['Maçã', 'Banana', 'Manga', 'Uva']

frutas.remove('Manga')
del frutas[-1]

print(frutas)

## OUTRA FORMA

frutas = ['Maçã', 'Banana', 'Manga', 'Uva']
frutas.remove('Manga')
del frutas[-1]

print(frutas)
'''

#DESAFIO DE LISTAS COM LOOP
'''
frutas = ['Maçã', 'Morango', 'Uva']

for x in frutas:
    print(f'Eu gosto de {x}')

## OUTRA FORMA

frutas = ['Maçã', 'Morango', 'Uva']

for fruta in frutas:
    print('Eu gosto de ' + fruta)
'''
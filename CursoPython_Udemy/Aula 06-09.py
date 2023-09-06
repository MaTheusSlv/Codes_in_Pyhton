#DESAFIO CONTANDO COM O FOR LOOP
'''
for numero in range(1,11):
    print(numero)

## OUTRA FORMA

for i in range(1,11):
    print(i)
'''

#DESAFIO DO NESTED FOR LOOPS
'''
frutas = ['Mamão', 'Banana', 'Abacate']
vegetais = ['Cenoura', 'Batata', 'Batata-doce']

for i in frutas:
    for x in vegetais:
        print(f'Fruta: {i}, Vegetal: {x}')

## OUTRA FORMA

frutas = ['Mamão', 'Banana', 'Abacate']
vegetais = ['Cenoura', 'Batata', 'Batata-doce']

for fruta in frutas:
    for vegetal in vegetais:
        print(fruta, vegetal)
'''

#DESAFIO WHILE LOOP
'''
x = 1

while x <= 10:
    print(x)
    x = x + 1

## OUTRA FORMA

numero=1

while numero<=10:
    print(numero)
    numero+=1
'''

#DESAFIO DO LOOP COM BREAK E CONTINUE
'''
print('Loop com o break: ')
for numero in range(1, 11):
    if numero > 5:
        break
    print(numero)
    
print('Loop com o continue: ')
for numero in range(1, 11):
    if numero == 5:
        continue
    print(numero)

## OUTRA FORMA

print('Loop com o break: ')
for numero in range(1,11):
    if numero>5:
        break
    print(numero)
    
print('Loop com o continue: ')
for numero in range(1,11):
    if numero==5:
        continue
    print(numero)
'''
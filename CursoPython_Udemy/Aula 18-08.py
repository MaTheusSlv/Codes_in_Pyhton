#NESTED LOOPS
'''
for numero1 in range(5):  #OUTER LOOP
    print(numero1)
    for numero2 in range(5):  #INNER LOOP
        print(numero2)

#Ele executará o INNER LOOP inteiro para cada vez que o OUTER LOOP executar
'''

#SEPARANDO STRINGS
'''
palavra=input('Escreva sua palavra:')

for espaco in palavra:
    print(f' {espaco}', end='') #O END com o '' indica que o print deve voltar para o FOOR LOOP sem imprimir na linha de baixo qunado ver um espaço vazio
'''

#FOR LOOP CRIANDO RETANGULO
'''
#Criar um retangulo de 6x6
# @@@@@@
# @@@@@@
# @@@@@@
# @@@@@@
# @@@@@@
# @@@@@@

linhas=6
colunas=6
simbolo='@'

for l in range(linhas):
    for c in range(colunas):
        print(simbolo, end='')
    print()
'''

#WHILE LOOPS
'''
#Criar promoção no valor de R$100,00, porém a cada compra ela vai ficar R$5 mais barata e não pode vender por menos de R$20

valor=100
dia=0

while valor > 20:
    dia+=1
    print(f'No dia {dia} o produto vai ser vendido por R${valor}')
    valor-=5

#WHILE LOOPS são ótimos para loops que dependem de condições
'''

#OPERADOR TERNÁRIO
'''
#Só pode votar se for maior de 16 anos

idade=14

if idade >= 16:
    resultado = print('Pode votar') #Você pode guardar o resultado de um loop numa variável
else:
    resultado = print('Não pode votar')

resultado='Pode votar' if idade >=16 else 'Não pode votar' #OPERADOR TERNÁRIO
'''

#DIFERENÇAS ENTRE OS LOOPS
'''
if else = Executa se verdadeiro ou falso e não se repete

for loop = Executa num número de vezes definido

while loop = Executa enquanto a condição for satisfeita
'''

#CONDIÇÕES COM WHILE LOOP
'''
#Aplicar comissão de 10% em produtos vendidos acima de R$20

valor=int(input('Digite o valor do seu produto em R$: '))

while valor > 20:
    valor = (valor * 0.10) + valor
    print(f'O valor final do seu produto será de R${valor}')
    break
'''
#OPERADORES MATEMÁTICOS
'''
calculo=2+2

print(calculo)

calculo=2+2*3/2 #Resultado=5
#Multiplicações e divisões são resolvidas da esquerda para direita com prioridade sobre outros operadores assim como numa equação
#E assim como numa equação, também, utilizasse os parenteses para que a operação seja feita antes dos operadores * e /
#Ex: (2+2)*3/2

#Exponenciais == 2**3 =8 (2*2*2=8)

#Então a ordem é: Parentesses > Exponêncial > Multiplicação e divisão > Soma e subtração
'''

#OPERADORES DE COMPARAÇÃO
'''
operadores=10 == 10

print(operadores)

# == igual
# != diferente
# > maior que
# < menor que
# >= maior ou igual a
# <= menor ou igual a

#Python é CASE SENSITIVE!

'''

#OPERADORES DE ATRIBUIÇÃO
'''
#Possibilita realizar contas matemáticas de forma mais simples

x=10
#x=x+5
x+=5 #15
x-=5 #5
x*=5 #50
x/+5 #2
x%=3 #1 #"quanto me sobra se eu preencher x com 3's"

print(x)
'''

#DECLARAÇÕES CONDICIONADAS
'''
velocidade=100

if velocidade >110:
    print('Acima da velocidade permitida')
    print('Reduza sua velocidade')
elif velocidade <60:
    print('Dirija acima de 60Km/h')
else:
    print('Velocidade OK')

#Você pode ter vários elif's dentro de uma declaração
'''

#OPERADORES LÓGICOS
'''
renda_acima_5mil= True
nome_limpo= False

if renda_acima_5mil and nome_limpo:  #No if pode-se colocar o "and" e o "or"
    print('Financiamento aprovado')
else:
    print('Financiamento negado')

#AND = E ; OR = OU
'''

#MULTIPLOS OPERADORES DE COMPARAÇÃO
'''
valor= 10

if valor >=20 and valor <40:
    print('Produto aceito')
else:
    print('Produto não aceito')

#OUTRA FORMA
valor= 20

if 20<= valor < 40:
    print('Produto aceito')
'''

#FOR LOOPS
'''
#Imprimir de 1 a 5

for numero in range(6):
    print(numero)

#"PYTHON SEMPRE CONTA PELO INDEX, COMEÇANDO SEMPRE DO 0"

#OUTRA FORMA AGORA INFORMANDO A RANGE, INÍCIO E FIM DO LOOP
for numero in range(1, 6):
    print(numero)

#VOCÊ PODE USAR O 'STEP(4 ali)' PARA IR PULANDO DE QUANTIDADE(STEP) EM QUANTIDADE(STEP)
for numero in range(1, 20, 4):
    print('numero')
'''

#FOR LOOPS COM STRINGS
'''
for letra in 'Google':
    print(letra)

G
o
o
g
l
e

palavra='Google'

for letra in palavra:
    print(f'{letra} está dentro da palavra {palavra})
'''

#FOR LOOPS COM IF ELSE
'''
#Enviar email com os detalhes da compra online

compra-confirmada= True
dados_compra= 'Compra no valor de R$12.50 e entrega confirmada'

for enviar in range(3):
    if compra_confirmada:
        print(dados_compra)
        print('Detalhes enviados para o seu email')
        break  #O BREAK faz pular pra fora do FOR LOOP se o IF for satisfeito
else:
    print('Falha na compra')
'''
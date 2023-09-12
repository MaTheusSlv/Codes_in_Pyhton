#DESAFIO PESQUISA DE PAÍS E CAPITAL
'''
paises = {'Brasil':'Brasilia', 'Argentina':'Buenos Aires', 'EUA':'Washington', 'Inglaterra':'Londres', 'Italia':'Roma'}
pais_usu = input('Digite o nome de um país: ')

if pais_usu in paises:
    print(f'A capital da(o) {pais_usu} é {paises[pais_usu]}')
else:
    print('Desculpe, não temos informações sobre a capital desse pais')

##  OUTRA FORMA

capitais = {'Brasil':'Brasilia', 'Argentina':'Buenos Aires', 'EUA':'Washington', 'Inglaterra':'Londres', 'Italia':'Roma'}
pais_usu = input('Digite o nome de um país: ')

if pais_usu in capitais:
    print(f'A capital da(o) {pais_usu} é {capitais[pais_usu]}')
else:
    print('Desculpe, não temos informações sobre a capital desse pais')
'''

#DESAFIO COMPARAÇÃO EM SETS
'''
amigos1 = {'Moacir','Matheus','Arthur','Luciana','Lucas'}
amigos2 = {'Jaqueline','Moacir','Lucas','Bruna','Paulo'}

amigos_em_comum=amigos1.intersection(amigos2)

print(amigos_em_comum)

##  OUTRA FORMA

amigos1={'Moacir','Matheus','Arthur','Luciana','Lucas'}
amigos2={'Jaqueline','Moacir','Lucas','Bruna','Paulo'}

result=amigos1.intersection(amigos2)

print(result)
'''

#DESAFIO FUNÇÕES SIMPLES
'''
def calculador():
    numero = int(input('Digite um número: '))
    resultado = numero ** 2
    print(resultado)

calculador()

##  OUTRA FORMA

def quadrado(numero):
    return numero**2

num = int(input('Digite um número: '))
print(f'O quadrado de {num} é {quadrado(num)}')
'''
#PRINT SERVE PARA EXTRAIR RESULTADOS PARA O CONSOLE
'''
print('Olá')
print("Tudo bem?")
'''
#COMENTÁRIOS

#Comentário single line
'''
Comentário
multi
line
'''

#TIPOS DE DADOS - DATA TYPES
'''
Text:
string = str("")

Numbers:
Integer = inteiro (1, 2, 3,...)
Float = fração (3.5, 4.7, 10.6)

Boolean:
Bool = true ou false
'''

#VARIÁVEIS
'''
#São containers para armazenar dados que podem ser utilizados em todo o código

x=2
y='Olá'

print(x)
print(x+x)
print(y)
'''

#MODIFICAÇÃO DE DADOS
'''
x=str(3)
y=int(4)
z=float(5)

print(x)
print(y)
print(z)

print(x+x) #33
print(y+y) #8
print(z+z) #10.0
'''

#STRINGS E INTEGERS
'''
#Criar frase e adicionar variáveis e imprimí-las

nome='Matheus'
idade=24 #ou idade=str(idade)
cidade='São Paulo'

print("O " + nome + " tem " + str(idade) + " anos e mora na cidade de " + cidade + ".")

#Python não concatena STR e INT, por isso converte-se
'''

#INPUT - INTERAÇÃO DO USUARIO COM O PROGRAMA
'''
nome=input('Qual é o seu nome: ')
idade=input('Qual é a sua idade: ')
cidade=input('Onde você mora: ')

print("O " + nome + " tem " + str(idade) + " anos e mora na cidade de " + cidade + ".")
'''

#PROGRAMA QUE INFORME O ANO QUE A PESSOA NASCEU
'''
ano_nascimento=input('Em que ano você nasceu? ')
idade=2023 - int(ano_nascimento)

print(idade)

# print(type(idade)) #Função TYPE diz qual o tipo de dado da variável
'''

#SLICING (Cortando)
'''
fruta='Abacate'
#Posição=index == 0- A ;1- b ;2- a ;3- c ;4- a ;5- t ;6- e

print(fruta[3]) #Uma letra
print(fruta[2:6]) #Um intervalo de caracteres
print(fruta[-1]) #Conta de trás para frente

valor=99.75
valor=str(valor) #Precisa converter porque o slicing só funciona com string
#Posição=index == 0- 9 ;1- 9 ;2- . ;3- 7 ;4- 5

print(fruta[0:2])
'''

#FORMATED STRINGS f'texto{variável}'
'''
nome='Matheus'
sobrenome='Silva'
profissao='Programador'
texto='O '+ nome +' '+ sobrenome + ' é um excelente ' + '['+profissao+']'
texto2=f'O {nome} {sobrenome} é um excelente [{profissao}]'

#O Matheus Silva é um excelente [programador]

print(texto)
print(texto2)
'''

#MÉTODOS PARA STRING
'''
#Métodos são meios de alterar strings

mensagem='Eu adoro comida caseira'

print(mensagem) #padrão
print(mensagem.lower()) #letra minúscula
print(mensagem.upper()) #letra maiúscula
print(mensagem.capitalize()) #1° letra para maiúscula
print(mensagem.find('c')) #retorna a posição da letra/palavra na string(-1 significa que não encontrou)
print(mensagem.replace('a', 'e')) #troca uma letra/palavra por outra informada
print(mensagem.strip()) #remove espaços que tenham antes do 1° caractere
'''
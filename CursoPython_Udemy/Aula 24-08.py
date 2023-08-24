#LISTAS
'''
#Permitem armazenar mais dados numa única variável

cidades = ['Rio de Janeiro', 'São Paulo', 'Salvador']

print(cidades)
'''

#MANIPULANDO LISTAS
'''
cidades = ['Rio de Janeiro', 'São Paulo', 'Salvador']
#indexes            0               1           2

numero= [2, 4, 6] #TAMBÉM PODE SER DE NÚMEROS

print(cidades[0]) #O [index] TRAZ O VALOR CORRESPONDENTE DA VARIÁVEL

print(numeros)

cidades[0] ='Brasília' #ALTERA O DADO DAQUELE INDEX DA VARIÁVEL
'''

#FUNÇÕES DENTRO DAS LISTAS
'''
cidades = ['Rio de Janeiro', 'São Paulo', 'Salvador']
#indexes            0               1           2

cidades.append('Santa Catarina') #O APPEND ADICIONA O VALOR INFORMADO NO FIM DA LISTA
cidades.remove('Salvador') #O REMOVE DELETA O VALOR INFORMADO DA LISTA
cidades.insert(1, 'Santa Catarina') #O INSERT INSERE O ITEM NA LISTA NA POSIÇÃO INDICADA(1)
cidades.pop(0) #O POP TAMBÉM APAGA
cidades.sort() #O SORT ORGANIZA EM ORDEM ALFABÉTICA OS ITENS DA LISTA

print(cidades)
'''

#CONCATENAÇÃO DE LISTAS
'''
numeros=[2, 3, 4, 5]
letras=['a', 'b', 'c', 'd']

final=numeros * 2
final2=numeros+letras
#OU
numeros.extend(letras) #O EXTEND CONCATENA LISTAS

print(final)

#LISTAS DENTRO DE LISTAS
itens=[['item1', 'item2'], ['item3', 'item4']]

print(itens[0][1])
'''

#EXTRAIR DADOS DE UMA LISTA E UTILIZAR NUMA VARIÁVEL
'''
produtos=['arroz', 'feijão', 'laranja', 'banana']

item1=produtos[0]
item2=produtos[1]
item3=produtos[2]
item4=produtos[3]
#OU
item1, item2, item3, item4 = produtos
#OU
item1, item2, item3, *outros = produtos

print(item1)
print(item2)
print(item3)
print(outros)
'''

#LOOPING DENTRO DE UMA LISTA
'''
valores=[50, 80, 110, 150, 170]

for x in valores:
    print(f'O valor final do produto é de R${x}')

'''

#VERIFICANDO ITENS DE UMA LISTA
'''
cor_cliente=input('Digite a cor desejada: ')
cores=['amarelo', 'verde', 'azul', 'vermelho']

if cor_cliente.lower() in cores:  #O LOWER() NORMALIZA O QUE O USUÁRIO DIGITAR PARA O PADRÃO DA LISTA
    print('Em estoque')
else:
    print('Essa cor não temos em estoque')
'''

#AGREGANDO DUAS LISTAS COM O ZIP
'''
cores=['amarelo', 'verde', 'azul', 'vermelho']
valores=[10, 20, 30, 40]

duas_listas= zip(cores, valores)

print(list(duas_listas))


var= list('comprar') #O LIST CONVERTE O VALOR DA VARIÁVEL EM UMA LISTA
print(var)
'''

#INPUT EM UMA LISTA
'''
frutas_usuario=input('Digite o nome das frutas separados por virgula: ')

frutas_lista= frutas_usuario.split(', ')

print(frutas_lista)
'''
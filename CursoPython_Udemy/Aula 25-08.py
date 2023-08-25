#TUPLES
'''
#TAMBÉM É UMA LISTA PORÉM, A FORMA COMO O PYTHON ARMAZENA E TRATA É DIFERENTE DE UMA LISTA
#OS ITENS DE UMA TUPLE NÃO PODEM SER ALTERADOS, ADICIONADOS OU REMOVIDOS
# []lists // ()tuple
cores_list=['amarelo', 'verde', 'azul', 'vermelho']
cores_tuple=('amarelo', 'verde', 'azul', 'vermelho')

print(type(cores_list))
print(type(cores_tuple))

duas_listas = cores_list * 2
print(duas_listas)
'''

#ARRAYS
'''
#NORMALMENTE USADA QUANDO UMA LISTA GRANDE ESTÁ ATRAPALHANDO O DESEMPENHO DO CÓDIGO

from array import array  #NÃO É PADRÃO NO PYTHON

letras=['a','b','c','d']
numeros_i=[10,20,30,40]
numeros_f=[1.2,2.2,3.2]

print(letras)
print(numeros_i)
print(numeros_f)

letras=array('u', ['a','b','c','d'])
numeros_i=array('i', [10,20,30,40])
numeros_f=array('f', [1.2,2.2,3.2])  #A ARRAY() CONVERTE A LISTA EM ARRAY

print(letras)
'''

#CRIANDO SETS
'''
#SIMILAR A LISTAS, EVITA DUPLICAÇÕES DE ITENS E NÃO UTILIZA INDEX

list1=[10, 20, 30, 40, 50]
list2=[10, 20, 60, 70]

num1=set(list1)
num2=set(list2)

print(num1 | num2) #UNION, JUNTA AS DUAS RETIRANDO OS VALORES REPETIDOS
print(num1 - num2) #DIFFERENCE, MOSTRA O QUE TEM EM UMA QUE NÃO TÊM NA OUTRA
print(num1 ^ num2) #SYMMETRIC DIFFERENCE, RETIRA OS PRESENTES NAS DUAS LISTAS
print(num1 & num2) #AND, TRÁS O QUE É DUPLICADO EM AMBAS AS LISTAS

print(len(num1)) #O LEN() TRÁS O TAMANHO DA LISTA
print(num1[0]) #NÃO FUNCIONA
'''

#FUNÇÕES EM SETS
'''
list1=set([1, 2, 3, 4, 5, 6])
s1 = {1, 2, 3, 4, 5, 6}
s1.add(7) #O .ADD() ADICIONA UM ITEM NUMA SET (SE ADICIONAR UM ITEM QUE JÁ TÊM ELE NÃO REPETE POR SER UM SET)
s1.update([7, 8, 9, 10]) #O .UPDATE() ADICIONA MAIS DE UM ITEM SEM REPETIR O QUE JÁ TÊM
s1.remove(10) #O .REMOVE() REMOVE UM ITEM DO SET
s1.discard(9) #O .DISCARD() DESCARTA UM ITEM QUE NÃO NECESSARIAMENTE ESTÁ NO SET, DIFERENTE DO .REMOVE() QUE PRECISA ESTAR

print(list1)
print(s1)
'''

#SETS COM STRINGS
'''
set1={'a', 'b', 'c'}
set2={'a', 'd', 'e'}
set3={'c', 'd', 'f'}

set4=set1.union(set2)
set5=set1.difference(set3)
set6=set1.intersection(set2) #O .INTERSECTION TRÁS APENAS OS ITENS QUE TÊM EM AMBOS OS SETS
set7=set1.symmetric_difference(set3)

print(set)
'''
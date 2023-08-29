#TRY E EXCEPT
'''
#EXCELENTE PARA TESTES, NÃO INTERROMPE A EXECUÇÃO DO PROGRAMA E PERMITE DAR UMA MENSAGEM PERSONALIZADA DE ERRO

try:
    letras=['a', 'b', 'c']
    print(letras[3])
except IndexError:
    print('Index não existe')
'''

#TRY E EXCEPT COM INPUT
'''
try:
    valor=int(input('Digite o valor do seu produto: '))
    print(valor)
except ValueError:
    print('Favor digitar um valor em números')
'''

#ELSE E FINALLY
'''
try:
    valor=int(input('Digite o valor do seu produto: '))
    print(valor)
except ValueError:
    print('Favor digitar um valor em números')
else:              #O ELSE SERÁ EXECUTADO SE NÃO TER EXCEPTION
    print('Usuário digitou um valor correto')
    resultado=valor * 2
    print(resultado)

print('mais código abaixo')

#OU

try:
    valor=int(input('Digite o valor do seu produto: '))
    print(valor)
except ValueError:
    print('Favor digitar um valor em números')
finally:              #O FINALLY SEMPRE SERÁ EXECUTADO INDEPENDENTE DE TER EXCEPTION OU NÃO
    print('Código OK')

print('mais código abaixo')
'''

#CLASSES
'''
#USADAS PARA CRIAR OBJETOS, SÃO USADAS PARA AGRUPAR DADOS E FUNÇÕES

nome='André'
nome_lower=nome.lower()

print(nome_lower)

#O '.' PERMITE QUE ACESSEMOS OS MÉTODOS DISPONÍVEIS
'''

#CRIANDO A PRIMEIRA CLASSE
'''
class Funcionarios:
    nome='Elena'
    sobrenome='Cabral'
    data_nascimento='12/01/2009'

usuario1 = Funcionarios()

print(usuario1.nome)
print(usuario1.sobrenome)
print(usuario1.data_nascimento)
'''

#CRIANDO OBJETOS DENTRO DE UMA CLASSE
'''
class Funcionarios: #CRIAR A CLASSE
    pass

usuario1 = Funcionarios() #CRIAR O OBJETO
usuario2 = Funcionarios()

usuario1.nome = 'Elena' #CRIAR OS PARÂMETROS DO USUARIO1
usuario1.sobrenome='Cabral'
usuario1.data_nascimento='12/01/2009'

usuario2.nome = 'Carol' #CRIAR OS PARÂMETROS DO USUARIO2
usuario2.sobrenome='Silva'
usuario2.data_nascimento='15/10/2005'

print(usuario1.nome)
print(usuario2.nome)
'''

#CONSTRUTORES
'''
class Funcionarios: #CRIAR A CLASSE
    def __init__(self, nome, sobrenome, data_nascimento): #O SELF INDICA QUE O PRÓPRIO OBJETO SERÁ USADO NA CONSTRUÇÃO
        self.nome= nome
        self.sobrenome= sobrenome
        self.data_nascimento= data_nascimento

usuario1 = Funcionarios('Elena', 'Cabral', '12/01/2009') #CRIAR O OBJETO
usuario2 = Funcionarios('Carol', 'Silva', '15/10/2005')

print(usuario1.nome)
print(usuario2.data_nascimento)
'''
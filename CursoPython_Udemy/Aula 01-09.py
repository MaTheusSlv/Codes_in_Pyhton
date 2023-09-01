#DESAFIO CALCULADORA PARA PINTURA (FUNÇÕES)
'''
rendimento_lata = int(input('Qual é o rendimento da lata? '))
altura = int(input('Qual é a altura da parede? '))
largura = int(input('Qual é a largura da parede? '))

def calcular():
    parede = altura * largura
    qtd_latas = parede / rendimento_lata
    print(f'Você necessita de {qtd_latas} lata(s) de tinta')

calcular()

## OUTRA FORMA

rendimento=int(input('Qual é o rendimento da lata? '))
largura=int(input('Qual é a largura da parede? '))
altura=int(input('Qual é a altura da parede? '))

def calculo_tinta():
    area=altura * largura
    total=area / rendimento
    print(f'Você necessita de {total} latas de tinta')

calculo_tinta()
'''

#DESAFIO FUNCIONÁRIOS EM UMA EMPRESA (SETS)
'''
funcionarios = set(['ana','marcos','alice','pedro','sophia','bruno','melissa'])
turno_dia = set(['ana','marcos','alice','melissa'])
turno_noite = set(['pedro','sophia','bruno'])
tem_carro = set(['marcos','alice','bruno','melissa'])

print(f'Funcionários que tem carro e trabalham à noite: {tem_carro & turno_noite}')
print(f'Funcionários que tem carro e trabalham durante o dia: {tem_carro & turno_dia}')
print(f'Funcionários que não tem carro: {funcionarios - tem_carro}')

## OUTRA FORMA

funcionarios = ['ana','marcos','alice','pedro','sophia','bruno','melissa']
turno_dia = ['ana','marcos','alice','melissa']
turno_noite = ['pedro','sophia','bruno']
tem_carro = ['marcos','alice','bruno','melissa']

lista1 = set(tem_carro).intersection(turno_noite)
print(lista1)

lista2 = set(tem_carro).intersection(turno_dia)
print(lista2)

lista3 = set(funcionarios).difference(tem_carro)
print(lista3)
'''
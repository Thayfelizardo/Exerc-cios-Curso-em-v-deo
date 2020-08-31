#FORMAS DE FAZER VARIAVEIS COMPOSTAS COM TUPLAS

lanche  = ('Hamburguer ', 'suco', 'pizza', 'pudim')
for c in lanche:
   print(f'Eu vou comer {c}')

 ############# OU ASSIM

lanche  = ('Hamburguer ', 'suco', 'pizza', 'pudim')

for cont in range(0, len(lanche)):
    print(lanche[cont])
print('Comi demais')


############# OU ASSIM

lanche  = ('Hamburguer ', 'suco', 'pizza', 'pudim')

for cont in range(0, len(lanche)):
    print(f'Vou comer {lanche[cont]}')
print('Comi demais')

############# OU ASSIM PARA INDICAR A POSIÇÃO
lanche  = ('Hamburguer ', 'suco', 'pizza', 'pudim')
for cont in range(0, len(lanche)):
    print(f'Vou comer {lanche[cont]} na posição {cont}')

############# OU ASSIM PARA INDICAR A POSIÇÃO TAMBÉM
lanche  = ('Hamburguer ', 'suco', 'pizza', 'pudim')
for pos, comida in enumerate(lanche):
    print(f'Vou comer {comida} na posição {pos}')


############# PARA ORGANIZAR AS TUPLAS EM ORDEM ALFABETICA
lanche  = ('Hamburguer ', 'suco', 'pizza', 'pudim')

print(sorted(lanche))

########### PARA MANIPULAR + DE UMA TUPLA
a = (2,5,8,9)
b = (6,4,1,9,7)
print(a+b)

#OU

a = (2,5,8,9)
b = (6,4,1,9,7)
c = a+b
print(c)

#OU PARA MOSTRAR QUANTOS ITENS TEM NO TOTAL DAS TUPLAS

a = (2,5,8,9)
b = (6,4,1,9,7)
c = a+b
print(len(c)

# OU PARA MOSTRAR QUANTAS VEZES APARECE DETERMINADO ITEM

a = (2, 5, 8, 9)
b = (6, 4, 1, 9, 7)
c = a + b
print(c.count(9))

######## PARA MOSTRAR A POSIÇÃO DE UM ITEM
a = (2, 5, 8, 9)
b = (6, 4, 1, 9, 7)
c = a + b
print(c)
print(c.index(9))

######## PARA MOSTRAR A POSIÇÃO DE UM ITEM SE POSSUI MAIS DE UM

a = (2, 5, 8, 9)
b = (6, 4, 1, 9, 7)
c = a + b
print(c)
print(c.index(9,4)) #SABENDO QUE JA POSSUI UM 9 NA POSIÇÃO 3, COLOCA-SE (9) PARA INDICAR O ITEM DESEJADO E O NUMERO DA PROXIMA POSIÇÃO APOS A ENCONTRADA, NESTE CASO SENDO (4) POIS JA POSSUI UM 9 NA POSIÇÃO 3


####PARA EXCLUIR UMA TUPLA ESPECIFICA

pessoa = ('Thayna', 24, 'F', 69.00)
del pessoa
print(pessoa)
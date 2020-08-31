## PARA REMOVER UM ITEM DA LISTA DE ACORDO COM A POSICÇÃO
del lanche [3]
# OU
lanche.pop(3)
# PARA REMOVER SOMENTE O ULTIMO ELEMENTO
lanche.pop()

#PARA REMOVER UM ITEM DA LISTA DE ACORDO COM O NOME DELE
lanche.remove('pizza')


## PARA ORDERNAR VALORES
valores.sort()#ordena em ordem crescente
valores.sort(reverse=True) #ordena em ordem decrescente

# DETERMINAS UM AÇÃO COM UMA CONDIÇÃO
if 'pizza' in lanche:
    lanche.remove('pizza')  # se tiver pizza na lista de lanche, remova pizza

#CRIAR UMA LISTA A PARTIR DE UM RANGE
valores= list(range(4,11)) # esse comando irá criar uma lista de 4 a 11 (excluindo o ultimo numero)

## SABER O TAMANHO DA LISTA
valores = [5,6,8,4,1,9,2,10]
len(valores)


### LISTAS PARTE 2 ####

#Lista dentro de lista
pessoas= [['Pedro',25], ['Maria',19], ['João',32]]


#PARA JUNTAR LISTAS
teste = list()
teste.append('Thayna')
teste.append(24)
print(teste)

#PARA COLOCAR UMA LISTA DENTRO DA LISTA
teste = list()
teste.append('Thayna')
teste.append(24)
galera = list ()
galera.append(teste)
print(galera)

##
teste = list()
teste.append('Thayna')
teste.append(24)
galera = list ()
galera.append(teste[:])
teste [0] = 'Rubem'
teste [1] = 31
galera.append(teste[:])
print(galera)

##ESTRUTURAS COMPOSTAS DENTRO DE LISTAS E IMPRIMINDO A LISTA TODA OU FRAGMENTADA
galera = [['Joao', 19],['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera[0])

galera = [['Joao', 19],['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera[0][1])

galera = [['Joao', 19],['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera[3])

galera = [['Joao', 19],['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera[3][1])

## SE QUISER PRINTAR UMA PARTE ESPECIFICA DE TODAS AS LISTAS DE ACORDO COM A POSIÇÃO DE FATIAMENTO
galera = [['Joao', 19],['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in galera:
    print(p[0])

galera = [['Joao', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')


## FORMANDO LISTAS APARTIR DE ENTRADA DE DADOS     OBS: O COMANDO [:] FAZ A COPIA DOS DADOS

pessoas = list()
dado = list ()
for c in range (0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    pessoas.append(dado[:])
    dado.clear()
print(pessoas)

## APLICANDO CONDIÇÕES

pessoas = list()
dado = list ()
totalmaior = totalmenor = 0
for c in range (0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    pessoas.append(dado[:])
    dado.clear()
for p in pessoas:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totalmaior+=1
    else:
        print(f'{p[0]} é menor de idade.')
        totalmenor += 1
print(f'Temos {totalmaior} maiores e {totalmenor} menores de idade')
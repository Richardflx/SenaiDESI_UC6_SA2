lista = [5,7,2,9,4,1,3]


# a) tamanho da lista
contador = 0
for item in lista:
    contador += 1
print(f'O tamanho da lista é de {contador} items.')


# b) maior valor
maior = 0
for item in lista:
    if item > maior:
        maior = item
print(f'O maior valor da lista é {maior}.')


# c) menor valor
menor = 999
for item in lista:
    if item < menor:
        menor = item
print(f'O menor valor da lista é {menor}.')


# d) soma dos valores
somas = 0
for item in lista:
    somas += item
print(f'A soma dos valores da lista é igual a {somas}.')


# e) lista em ordem crescente
for passagem in range(len(lista)-1, 0, -1):
    for num in range(passagem):
        if lista[num] > lista[num+1]:
            lista[num+1], lista[num]  = lista[num], lista[num+1]
print(f'Lista em ordem crescente: {lista}')


# f) lista em ordem decrescente
for passagem in range(len(lista)-1, 0, -1):
    for num in range(passagem):
        if lista[num] < lista[num+1]:
            lista[num+1], lista[num]  = lista[num], lista[num+1]
print(f'Lista em ordem decrescente: {lista}')
lista = [5,7,2,9,4,1,3]

# a) tamanho da lista
print(f'O tamanho da lista é de {len(lista)} items.')

# b) maior valor
print(f'O maior valor da lista é {max(lista)}.')

# c) menor valor
print(f'O menor valor da lista é {min(lista)}.')

# d) soma dos valores
print(f'A soma dos valores da lista é igual a {sum(lista)}.')

# e) lista em ordem crescente
lista.sort()
print(f'Lista em ordem crescente: {lista}')

# f) lista em ordem decrescente
lista.reverse()
print(f'Lista em ordem decrescente: {lista}')
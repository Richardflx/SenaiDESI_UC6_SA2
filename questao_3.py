valores = list()

for contador in range (0, 20):
    valores.append(int(input("Digite um valor: ")))

print(f'Você digitou os valores :{valores}')

# A) maior valor
maior = 0
for item in valores:
    if item > maior:
        maior = item
print(f'O maior valor digitado foi {maior}.')


# B) menor valor
menor = 999999
for item in valores:
    if item < menor:
        menor = item
print(f'O menor valor digitado foi {menor}.')


# C) media dos valores
media = 0
for item in valores:
    media += item
media = media / len(valores)
print(f'A média dos valores é {media}.')

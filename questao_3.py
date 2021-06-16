valores = list()

for contador in range (0, 20):
    valores.append(int(input("Digite um valor: ")))

print(f'Você digitou os valores :{valores}')
print()
valores_media = sum(valores)/len(valores)

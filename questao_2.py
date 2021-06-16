valores = list()

for contador in range (0, 4):
    valores.append(int(input("Digite um valor: ")))

print(f'Você digitou os valores :{valores}')
print()
valores_media = sum(valores)/len(valores)
if valores_media > 0:
    print(f'Média positiva > {valores_media}')
elif valores_media < 0:
    print(f'Média negativa > {valores_media}')
else:
    print('Resultado 0')
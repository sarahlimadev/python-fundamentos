# 3. Faça uma lista de números de 1 a 10 e crie outra lista apenas com os números pares
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []

for numeros in numeros:
    if numeros % 2 == 0:
        pares.append(numeros)

print(pares)
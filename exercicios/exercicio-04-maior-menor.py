# 4. Crie uma função que recebe uma lista de números e retorna o maior e o menor valor (use tupla!)
def maior_menor(numeros):
 maior = max(numeros)
 menor = min(numeros)
 return (maior, menor)

print(maior_menor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
# 5. Crie uma função que recebe um nome e retorna quantas vogais ele tem
def contar_vogais(nome):

    vogais = "aeiouAEIOU"
    contador = 0

    for letra in nome:
        if letra in vogais:
            contador = contador + 1
    return contador

print(contar_vogais("Anderson"))
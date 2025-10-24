# 1. Crie uma lista com 5 números e calcule a soma de todos eles usando um loop for
anodenascimento = [1968, 1970, 1997, 2001, 2003]
soma = 0
for anodenascimento in anodenascimento:
    soma = soma + anodenascimento
    print(soma)


# 2. Crie uma lista com nomes de amigos e imprima apenas os nomes que têm mais de 5 letras
amigos = ["Leonilda", "Salomão", "Saulo", "Anderson"]
len(amigos)
for amigos in amigos:
    if len(amigos) > 5:
     print(amigos)


# 3. Faça uma lista de números de 1 a 10 e crie outra lista apenas com os números pares
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []
for numeros in numeros:
    if numeros % 2 == 0:
        pares.append(numeros)
        print(pares)


# 4. Crie uma função que recebe uma lista de números e retorna o maior e o menor valor (use tupla!)
def maior_menor(numeros):
 maior = max(numeros)
 menor = min(numeros)
 return (maior, menor)
print(maior_menor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


# 5. Crie uma função que recebe um nome e retorna quantas vogais ele tem
def contar_vogais(nome):
    vogais = "aeiouAEIOU"
    contador = 0
    for letra in nome:
        if letra in vogais:
            contador = contador + 1
    return contador
print(contar_vogais("Anderson"))
      

# 6. Faça uma função que recebe uma temperatura em Celsius e retorna Fahrenheit e Kelvin (retorno múltiplo!)
def converter_temperatura(celsius):
    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15
    return (fahrenheit, kelvin)
print(converter_temperatura(25))


# 7. Crie um dicionário com dados de um livro (título, autor, ano, páginas) e imprima essas informações formatadas
Livro = {
    "título": "O Alquimista",
    "autor": "Paulo Coelho",
    "ano": 1988,
    "páginas": 208
}
for chave, valor in Livro.items():
    print(f"{chave}: {valor}")


# 8. Faça um dicionário com 5 produtos e seus preços. Calcule o valor total
produtos = {
    "Feijão": 7.5,
    "Arroz": 5.0,
    "Macarrão": 4.0,
    "Cuscuz": 2.0,
    "Farinha": 3.5
}
for chave, valor in produtos.items():
    print(f"{chave}: {valor}")
    total = sum(produtos.values())
    print(f"Valor total: R$ {total}")


# 9. Crie uma lista de dicionários representando 3 alunos (nome, idade, nota) e calcule a média da turma
alunos = [ 
    {"nome": "Leonilda", "idade": 56, "nota": 10},
    {"nome": "Salomão", "idade": 55, "nota": 9},
    {"nome": "Saulo", "idade": 28, "nota": 8}
]
soma_notas = 0
for aluno in alunos:
    soma_notas = soma_notas + aluno["nota"]
    media = soma_notas / len(alunos)
    print(f"Média da turma: {media}")


# 10. Faça uma função que recebe uma lista de palavras e retorna um dicionário com a contagem de letras de cada palavra
def contar_letras(palavras):
    resultado = {}
    for palavra in palavras:
        resultado[palavra] = len(palavra)
    return resultado
lista_palavras = ["python", "programação", "código", "lista", "dicionário"]
contagem = contar_letras(lista_palavras)
print(contagem)
for palavra, qtd_letras in contagem.items():
    print(f"'{palavra}' tem {qtd_letras} letras")
# 10. Faça uma função que recebe uma lista de palavras e retorna um dicionário com a contagem de letras de cada palavra
palavras = ["python", "programação", "código", "lista", "dicionário"]

def contar_letras(palavras):
    resultado = {}
    for palavra in palavras:
        resultado[palavra] = len(palavra)
    return resultado

contagem = contar_letras(palavras)
print(contagem)

for palavra, qtd_letras in contagem.items():
    print(f"{palavra} tem {qtd_letras} letras")
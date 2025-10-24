# 7. Crie um dicionário com dados de um livro (título, autor, ano, páginas) e imprima essas informações formatadas
Livro = {
    "título": "O Alquimista",
    "autor": "Paulo Coelho",
    "ano": 1988,
    "páginas": 208
}

for chave, valor in Livro.items():
    print(f"{chave}: {valor}")
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
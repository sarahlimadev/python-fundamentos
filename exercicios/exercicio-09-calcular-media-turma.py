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
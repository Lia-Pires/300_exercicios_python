"""
49 - Crie um programa que recebe dados de um aluno como nome e suas notas 
em supostos 3 trimestres de aula, retornando um novo dicionário com o nome 
do aluno e a média de suas notas:
"""

aluno = [{"Nome": "Juarez", "Notas": [75, 80, 67]}]


def media_aluno(aluno):
    notas = []
    for media in aluno:
        if len(media["Notas"]) > 0:
            temp = round(sum(media["Notas"]) / len(media["Notas"]))
        else:
            temp = 0
        notas.append({"Nome": media["Nome"], "Média das notas": temp})
    print(notas)


media = media_aluno(aluno)

"""
46 - A partir de um simples dicionário composto por três intens, {"Alto Nível": "Python", "Médio Nível" : "C, "Baixo Nível": "Assembly"},
verifique se "Python"consta no dicionário em questão, utilizando de negação lógica para tal verificação:
"""


dicionario = {"Alto Nivel": "Python", "Medio Nivel": "C", "Baixo Nivel": "Assembly"}

for i in dicionario.values():
    if not i == "Python":
        print(f"Python não está na lista")
    else:
        print(f"Python está na lista")
    break

"""
50 - Crie um sistema de perguntas e respostas que interage com o usuário,
pedindo que o mesmo insira uma resposta.
Caso a primeira questào esteja correta, exiba em tela uma mensagem de acerto
e parta para a próxima pergunta, caso incorreta, exiba uma mensagem de erro e pule para a próxima pergunta:
"""


base = {
    "Pergunta 01": {
        "Pergunta": "Quanto é 2+2?",
        "Alternativas": {"a": "3", "b": "5", "c": "4", "d": "9"},
        "Resposta_correta": "c",
    },
    "Pergunta 02": {
        "Pergunta": "Quanto é 3x3?",
        "Alternativas": {"a": "9", "b": "6", "c": "1", "d": "7"},
        "Resposta_correta": "a",
    },
    "Pergunta 03": {
        "Pergunta": "Quanto é 2^2?",
        "Alternativas": {"a": "9", "b": "12", "c": "4", "d": "13"},
        "Resposta_correta": "c",
    },
    "Pergunta 04": {
        "Pergunta": "Quanto é 9x9?",
        "Alternativas": {"a": "81", "b": "64", "c": "98", "d": "99"},
        "Resposta_correta": "a",
    },
}


respostas_corretas = 0

for pkeys, pvalues in base.items():
    print(f'{pkeys}: {pvalues["Pergunta"]}')

    for rkeys, rvalues in pvalues["Alternativas"].items():
        print(f"[{rkeys}]:{rvalues}")

    resposta = input("Escolha uma alternativa: a, b, c ou d\n")

    if resposta == pvalues["Resposta_correta"]:
        print("Resposta Correta!!")
        respostas_corretas += 1
    else:
        print("Resposta incorreta!")

    if respostas_corretas == 0:
        print("Você não acertou nenhuma pergunta!")
    elif respostas_corretas == 1:
        print("Você acertou uma questão!")
    else:
        print(f"Você acertou {respostas_corretas} questões!")

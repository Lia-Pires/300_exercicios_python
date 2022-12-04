"""
25 - Peça para que o usuário digite um número, em seguida exiba em tela uma mensagem dizendo se tal número é PAR ou ÍMPAR:
"""

num = int(input("Digite um número: "))

if (num % 2) == 0:
    print(f"O número digitado ({num}) é PAR.")
else:
    print(f"O número digitado ({num}) é ÍMPAR.")

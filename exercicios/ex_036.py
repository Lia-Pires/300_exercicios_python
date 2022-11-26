"""
Crie um programa que pede que o usuário digite um nome ou uma frase, verifique se esse conteúdo digitado é um palindromo ou não, exibindo em tela esse resultado:
"""


palavra = input("Digite uma palavra ou frase: ")

inverter = palavra[::-1]

if inverter.lower().strip().replace(" ", "") == palavra.lower().strip().replace(
    " ", ""
):
    print(f"{palavra} é um palíndromo!")

else:
    print(f"{palavra} não é um palíndromo!")

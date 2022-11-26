"""
Crie um programa que pede ao usuário que o mesmo digite um número qualquer, em seguida retorne se esse número é primo ou não, caso não, retorne também quantas vezes esse número é divisível:
"""

num = int(input("Digite um número: "))
div = 0

for i in range(1, num + 1):
    if num % i == 0:
        div += 1

if div == 2:
    print(f"{num} é primo.")
    print(f"{num} é divisível apenas por 1 e por {num}.")

else:
    print(f"{num} não é primo.")
    print(f"{num} é divisível por {div} números")

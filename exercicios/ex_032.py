'''
32 - Crie um programa que exibe em tela a tabuada de um determinado número fornecido pelo usuário:
'''

num = int(input("Digite um número para conseguir sua tabuada: "))

for i in range(0,11):
    print(f"{num} x {i} = {num * i}")
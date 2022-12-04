"""
29 - Crie um programa que lê um valor de início e um valor de fim, exibindo em tela a contagem dos números dentro desse intervalo.
"""
inicio = int(input("Digite o valor de inicial: "))
fim = int(input("Digite o valor final: "))

for i in range(inicio, fim + 1):
    print(i)

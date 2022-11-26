"""
34 - Crie um programa que realiza a contagem de 1 até 100, usando apenas números
 ímpares, ao final do processo exiba em tela quantos números ímpares foram encontrados 
 nesse intervalo, assim como a soma dos mesmos:
"""

cont = 0
soma = 0

for i in range(1, 101, 2):
    cont += 1
    soma += i

print(f"Entre 1 e 100 existem {cont} números ímpares")
print(f"A soma de números ímpares entre 1 e 100 é {soma}")

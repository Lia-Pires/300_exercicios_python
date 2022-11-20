""" 
31 - Crie um programa que realiza a progressão aritmética de 20 elementos, com primeiro termo e razão definidos pelo usuário:
"""

# an = a1 + (n-1) * r
print("Para criar uma progressão aritmética de 20 elementos: ")

a = int(input("Digite o primeiro termo: "))
r = int(input("Digite a razão: "))


for n in range(1, 21):
    an = a + (n - 1) * r
    print(an)

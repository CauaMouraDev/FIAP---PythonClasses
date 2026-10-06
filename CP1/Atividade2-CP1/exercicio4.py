import os
os.system("cls")

idade = int(input("Digite sua idade:"))
altura = float(input("Digite sua altura:"))

if (idade >= 12 and altura >= 1.40):
    print("Autorizado a entrada no brinquedo")

else:
    print("Não autorizado")
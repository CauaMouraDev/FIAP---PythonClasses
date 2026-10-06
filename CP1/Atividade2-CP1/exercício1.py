import os
os.system("cls")

n1 = int(input("Digite sua primeira nota: "))
n2 = int(input("Digite sua segunda nota: "))

med = (n1 + n2)/2

print("Sua média é {}".format(med))

if (med >= 5 and med < 7):
    print("SITUAÇÃO: Você está de recuperção !")

elif (med < 5):
    print("SITUAÇÃO: Você foi diretamente reprovado !")

elif (med >= 7):
    print("SITUAÇÃO: PARABÉNS, VOCÊ FOI APROVADO !!!")
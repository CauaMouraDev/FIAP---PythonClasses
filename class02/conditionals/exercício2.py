import os
os.system("cls")

dinheiro = int(input("Digite o valor da compra:"))

if (dinheiro > 1000):
    dinheiro = dinheiro*0.9
    print(dinheiro)

else:
    print(dinheiro*0.95)
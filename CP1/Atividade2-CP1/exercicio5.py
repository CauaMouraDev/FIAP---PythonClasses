import os
os.system("cls")

temperatura = float(input("Digite a temperatura em °C: "))

if temperatura < 10:
    print("Classificação: FRIO")
elif 10 <= temperatura <= 20:
    print("Classificação: AMENO")
elif 20 < temperatura <= 25:
    print("Classificação: QUENTE")
else:
    print("Classificação: MUITO QUENTE")

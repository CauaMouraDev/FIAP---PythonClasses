import os
os.system("cls")

salario = float(input("Digite o salário: R$ "))
anos = int(input("Digite a quantidade de anos trabalhados: "))

if anos >= 5:
    if salario <= 3000:
        bonus = salario * 0.10
        print(f"Bônus: R$ {bonus:.2f}")
        print(f"Salário com bônus: R$ {salario + bonus:.2f}")
    else:
        bonus = salario * 0.07
        print(f"Bônus: R$ {bonus:.2f}")
        print(f"Salário com bônus: R$ {salario + bonus:.2f}")
else:
    bonus = salario * 0.03
    print(f"Bônus: R$ {bonus:.2f}")
    print(f"Salário com bônus: R$ {salario + bonus:.2f}")

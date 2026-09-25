import os
os.system("cls")

compra = float(input("Digite o valor da sua compra: "))

if (compra < 100.00):
    desc = compra + 0
    print(f"Seu valor se manteve em{desc}.Você não teve desconto!")

elif (compra >=100.00 and compra <= 499.99):
     desc = compra* 0.95
     print(f"Seu valor final ficou em {desc}")
     

elif (compra >=500 ):
     desc = compra* 0.90
     print(f"Seu valor final ficou em {desc}")

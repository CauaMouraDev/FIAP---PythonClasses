import os
os.system("cls")

valor = int(input("Valor: "))

match valor:
    case 1 | 3: # if valor == 1 or valor == 3:
        print("Digitou impar")
    case 2 | 4:
        print("Digitou par")
    case _:
        print("Digite um valor válido")
        

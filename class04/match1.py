import os
os.system("cls")

valor = int(input("Valor: "))

match valor:
    case 1:
        print("Digitou um")
    case 2:
        print("Digitou dois")
    case 3:
        print("Digitou três")
    case 4:
        print("Digitou quatro")
    case _:
        print("Digite um valor válido")
        

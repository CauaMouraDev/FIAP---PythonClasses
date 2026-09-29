import os
os.system("cls")

valor = input("Valor: ")
correto = True # flag -> variavel que controla um programa

match valor:
    case '1' | '3': # if valor == 1 or valor == 3:
        print("Digitou impar")
        valor = int(valor)
    case '2' | '4':
        print("Digitou par")
        valor = int(valor)
    case _:
        print("Digite um valor válido")
        correto = False

if correto:        
    dobro = valor + valor
    print ("Dobro: ", dobro)
import os
os.system("cls")

valor = int(input("Digite um valor: "))
#PARA OS CASOS APENAS DE 1 A 4!

match valor:
     case 1:
         print("Digitou impar !")
     case 2:
         print("Digitou par !")
     case 3:
         print("Digitou impar !")
     case 4:
         print("Digitou par !")
     case _:
         print("Digite um valor válido!")


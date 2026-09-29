import os
os.system("cls")

valor = int(input("Que mês estamos: "))
#PARA OS CASOS APENAS DE 1 A 4!

match valor:
     case 1:
          print("\033[32m Janeiro \033[0m")
     case 2:
         print("Fevereiro !")
     case 3:
         print("Março!")
     case 4:
         print("Abril !")
     case 5:
         print("Maio !")
     case 6:
         print("Junho !")
     case 7:
         print("Julho !")
     case 8:
         print("Agosto !")
     case 9:
         print("Setembro !")
     case 10:
         print("Outubro !")
     case 11:
         print("Novembro!")
     case 12:
         print("Dezembro !")
    
 

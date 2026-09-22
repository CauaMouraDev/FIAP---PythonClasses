import os
os.system("cls")

nota = float(input("Digite a nota"))

if nota >= 0:
    if nota <= 10:
        print("Nota válida!")
    else: 
         print("Nota inválida!")  


#========
if nota >= 0 and nota <= 10:
    print("Nota válida")

else:
    print("Nota inválida!")
        
import os
os.system("cls")
import sys



sal = float(input("Entra com seu salário: "))

if sal <= 0:
    print("ERRO ! Formato inválido, digite um valor positivo!")
    sys.exit()


fal = int(input("Seus dias de faltas: "))
min = 1302.00



print( "SALÁRIO:",sal)
print("FALTAS:",fal)


if sal >= 0 and sal <= (min*2):
    sal = sal * 1.0645
    print("Seu salário será reajustado para --->", sal)

elif sal > (min*2) and sal <= (min*5):
    sal = sal * 1.0455
    print("Seu reajuste será para ---> ",sal)

elif sal > (min*5) and sal <= (min*10):
    sal = sal * 1.0289
    print("Seu reajuste será para --->", sal)

elif sal > (min*10):
    print("Não terá reajuste")


if fal == 0:
    sal = sal + min
    print(" COM BÔNUS:",sal)

elif fal == 1:
    sal = sal + 500
    print(" COM BÔNUS:",sal)

elif fal > 1:
    print("Sem bônus")






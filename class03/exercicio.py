import os
os.system("cls")

n = int(input("Digitr um número: "))

if n < 0:
    print("O NÚMERO É NEGATIVO")
else:
    if n > 0:
       print("O número é negativo")

# ------ forma Elif  

if n < 0:
    print("Número é Negativo")

elif n > 0:
     print("Número é Positivo")

else:
    print("O número é nulo")
n1 = float(input("Digite a Nota1: "))

if n1 >= 0 and n1 <= 10:
    n2 = float(input("Digite a nota2 :"))

    if n2 >= 0 and n2 <= 10:
        media = (n1 + n2)/2
        print(f"A média é{media}")

    else:
        print("nota2 inválida")
else:
     print("nota 1 inválida")


#====== exercício3.1

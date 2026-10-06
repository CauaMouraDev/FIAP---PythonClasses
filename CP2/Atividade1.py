num = int(input("Início: "))
num2 = int(input("Fim: "))

if num > num2:
    print("[", end="")
    for i in range(num, num2 - 1, -1):
        print(i, end=", ")
    print("]")

elif num == num2:
    print("[",num,"]")
    print("Os números são iguais.")

elif num < num2:
    print("[", end="")
    for i in range(num, num2 + 1):
        print(i, end=", ")
    print("]")
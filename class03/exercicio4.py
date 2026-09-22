n1 = 10
n2 = 5

n2 = int(input("Digite o número2 :"))
n3 = int(input("Digite o número3:"))

if n1 >= n2 and n1 >= n3:
    print("Maior", n1)

elif n2 >= n1 and n2 >= n3:
    print("Maior:", n2)

else:
    print("Maior", n3)


import os
os.system("cls")
#==== Exercise - 1 ====
inteiro = int(input("Digite um número inteiro: "))
print("Antecessor:", (inteiro - 1))
print("Seu número:", (inteiro))
print("Sucessor:", (inteiro + 1))


#==== Exercise - 2 ====


med = float(input("Digite um valor em metros:"))

cent = med * 100

print(f"seu valor em centímetros é {cent} cm")


#====  Exercise - 3 ====

comp = float(input("Digite o comprimento do terreno: "))
larg = float(input("Digite a largura da terreno: "))

Ar = comp * larg

print(f"A área do terreno é {Ar} m²")

# ==== Exercício 4 ====


dh = float(input("Digite o seu ganho por hora trabalhada:"))

h = float(input("Digite a quantidade de horas trabalhada:"))


print("Seu salario mensal é R$", dh * h)


#==== Exercício 5 ====
prd = input("Digite o nome do produto:")
prc = float(input("Digite o preço d produto: "))
qnt = int(input("Digite a quantidade de unidades:"))
dsct = float(input("Digite o desconto: "))

vlr_b = prc * qnt
print("Valor bruto é: ",vlr_b)
vlr_d = (prc * qnt)* (dsct/100)
print(vlr_d)
vf = vlr_b * (1 - (dsct/100)) 

print(vf)


#==== Exercício 6 ====

min = int(input("Digite uma quantidade certa de minutos : "))

m = min - 60


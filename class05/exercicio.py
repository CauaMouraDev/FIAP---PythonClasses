#dado o valor inicial e final pelo usuario, exiba os numeros do intervalo fechado
#entrada: 4         9          saida: 4 5 6 7 8 9
# entrada: 4    9    saida: [4, 5, 6, 7, 8, 9]
#
# dado o valor inicial e final pelo usuario, exiba os numeros do intervalo aberto
# entrada: 4   9    saida: 5 6 7 8
#exiba no formato matematico:
# entrada: 4   9   saida: ]4, 5, 6, 7, 8, 9

#)(1)

inicio = int(input("Digite o valor inicial: "))
fim = int(input("Digite o valor final: "))

for i in range(inicio, fim + 1):
    print(i, end=" ")

#(2)

inicio2 = int(input("\nDigite o valor inicial: "))
fim2 = int(input("Digite o valor final: "))
print(end="[")
for i2 in range(inicio2 + 1, fim2):
    print(i2, end=",")


print( end="]")
fim = int(input("Digite o número final: "))
soma = 0

for numero in range(1, fim + 1):
    if numero % 2 == 0:
        soma += numero

print(f"A soma dos números pares de 1 até {fim} é: {soma}")

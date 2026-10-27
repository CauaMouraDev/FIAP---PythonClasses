# CRIANDO FUNÇÃO SOMA() E SOMANDO

def soma(lista):
    total = 0
    for numero in lista:
        total += numero
    return total


v = [0, 0, 0, 0, 0]

for i in range(0, 5):
    v[i] = int(input(f"Digite um número para a posição {i}: "))

resultado = soma(v)

print(v)
print(f"A soma dos valores é: {resultado}")

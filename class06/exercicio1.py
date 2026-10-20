# import secrets

# bruh = secrets.token_hex(100000000)
# print(bruh)


soma = 0
quantidade = 0

while True:
    nota = float(input("Digite a nota (-1 para sair): "))

    if nota == -1:
        break

    if nota < 0 or nota > 10:
        print("Nota inválida! Digite um valor entre 0 e 10.")
        continue

    soma += nota
    quantidade += 1

    media = soma / quantidade
    print(f"Média atual: {media:.2f}")

    if quantidade >= 3 and media >= 7:
        print("Você está aprovado!")
    elif quantidade >= 3 and media < 7:
        print("Você está reprovado!")
    else:
        print("Ainda faltam notas para avaliar.")
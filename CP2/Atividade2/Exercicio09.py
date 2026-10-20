texto = input("Digite uma palavra ou frase: ").lower()
vogais = "aeiou"
quantidade = 0

for letra in texto:
    if letra in vogais:
        quantidade += 1

print(f"A quantidade de vogais é: {quantidade}")

letra = input("Digite uma letra: ")


match letra:
      case 'a' | 'e' | 'i' | 'o' | 'u':
            print("vogal")

      case "b" | "c" | "d" | "f" | "g" | "h" | "j" | "k" | "l" | "m" | "n" | "p" | "q" | "r" | "s" | "t" | "v" | "w" | "x" | "y" | "z":
         print("consoantes")

      case _:
         print("{} é um caracter especial".format(letra))


#------- OUTRO MÉTODO ---------
# vogais = ['a', 'e', 'i', 'o', 'u']
# consoantes = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]

# letra = input("Digite uma letra: ").strip().lower()

# if letra in vogais:
#     print("vogal")
# elif letra in consoantes:
#     print("consoante")
# else:
#     print(f"{letra} é um caracter especial")
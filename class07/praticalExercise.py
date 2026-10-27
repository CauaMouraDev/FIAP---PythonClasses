v = [45, (89 * -1), 32, (12 * -1), 33]
print(v[0])

soma = 0
media = 0
for n in v:
    if n < 0:
        print(f"Número negativo: {n}")
    soma += n

media = soma/ len(v)
print(media)
    

print(f"Soma total: {soma}")

for i in v:
    if i % 2 != 0:
        print(i , end=" | ")

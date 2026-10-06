# 3. Dado um número pelo usuário, exibir os seus 10 próximos multiplos
# ENTRADA: 4    SAÍDA: 4 9 12 16 20 24 28 32 36 40

# 4. Dado um número pelo usuário e o multiplicador M, exibir os seus M próximos multiplos
# ENTRADA: 4  5  SAÍDA: 4 9 12 16 20

# 5. Dados 5 números pelo usuário, contar quantos são pares
# ENTRADA: 67 44 22 34 99  SAÍDA: 3 NÚMEROS SÁO PARES
import os
os.system("cls")

#(3)

numero = int(input("Digite um número: "))

for i in range(2, 11):
    print(i * numero, end=",")


#(4)

numero = int(input("\nDigite um número: "))
m = int(input("Digite o multiplicador M: "))

for i in range(1, m + 1):
    print(i * numero, end=",")


#(5)

cnt = 0
pares = 0
while cnt < 5:
    numero = int(input("\nDigite um número: "))
    if numero % 2 == 0:
        pares += 1
    cnt += 1

print(f"\nForam digitados {pares} números pares.")
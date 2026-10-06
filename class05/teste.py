
import os
os.system("cls")

import sys
num = int(input("Digite um número inicial: "))
num2 = int(input("Digite um número final: "))

if num >= num2:
    sys.exit("O número inicial deve ser menor que o número final.")

#Mostra intervalo de números entre num e num2
for i in range(num + 1, num2 ):
    print(i, end=" ")


while True:
    try:# TRY serve para tentar executar o código e caso ocorra algum erro, ele será tratado no bloco EXCEPT.
        num3 = int(input("\nDigite um número para verificar se ele está no intervalo: "))
        if num3 > num and num3 < num2:
            print(f"O número {num3} está no intervalo entre {num} e {num2}.")
        else:
            print(f"O número {num3} não está no intervalo entre {num} e {num2}.")
    except ValueError:# O bloco EXCEPT é executado quando ocorre um erro no bloco TRY. Nesse caso, ele captura o erro ValueError, que ocorre quando a conversão para inteiro falha.
        print("Por favor, digite um número válido.")
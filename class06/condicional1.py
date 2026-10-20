import os
os.system('cls')

opçao = 's'

while opçao == 's' or opçao == 'S':
     num = int(input("Digite um número:"))
     dobro = num * 2
     print(f"O dobro do número é{dobro}")
     
     opcao = int(input("Digite (s)im ou (n)ão para continuar:"))
     qtd = qtd + 1

     if opcao == 'n' or opcao == 'N':
          break 
    
print(f"Você calculou {qtd} de voltas!")
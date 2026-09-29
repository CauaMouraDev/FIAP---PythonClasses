valor = int(input("Digite um valor:"))
valor2 = int(input("Digite um segundo valor:"))
sinal = input("Digite o sinal de operação: ")


match sinal:
     case '/':
          rslt = valor / valor2
          print(rslt)
    
     case '*':
          rslt = valor * valor2
          print(rslt)
    
     case '+':
          rslt = valor + valor2
          print(rslt)
    
     case '-':
          rslt = valor - valor2
          print(rslt)

    
     case '**':
          rslt = valor**valor2
          print(rslt)

    
     case '//':
          rslt = valor // valor2
          print(rslt)

    
     case '%':
          rslt = valor % valor2
          print(rslt)

     case _:
          print("Operador inválido !")

    


    
    
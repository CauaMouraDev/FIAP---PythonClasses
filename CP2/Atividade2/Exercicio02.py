while True:
     opc = input("Digite uma opção: \nmult-> * \n soma-> +\n subs-> -\n div-> / \n Exit-> X ---- Responda:")
     
     if opc == "X":
          break
    
     num1 = float(input("Digite um número: "))
     num2 = float(input("Digite um número:"))
     match opc:
          case "*":
                rslt = num1 * num2
                print(rslt)
               
          case "+":
                rslt = num1 + num2
                print(rslt)
               
          case "-":
                rslt = num1 - num2
                print(rslt)
               
          case "/":
              if num2 == 0:
                  print("Não é possível divisão por 0")
                  break
              else:
                   rlst = num1 / num2
                   print(rslt)
    

        
               
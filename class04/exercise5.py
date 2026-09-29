placa = int(input("Digite os três últimos digitos da placa do seu carro:"))

x = placa % 10

match placa:
      case 1 | 2:
             print(f"{x}")
            
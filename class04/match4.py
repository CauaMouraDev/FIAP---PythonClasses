import os
os.system("cls")

print("""
1 - Cadastrar
2 - Consultar
3 - Editar
4 - Excluir
0 - SAIR
      """)
opcao = input("Escolha: ")

match opcao:
    case '0':
        ...
    case '1': 
        print("Comandos relacionados ao cadastro")
    case '2': 
        print("Comandos relacionados ao consulta")
    case '3': 
        print("Comandos relacionados a edição")
    case '4': 
        print("Comandos relacionados a exclusao")
    case _:
        print("opção inválida")

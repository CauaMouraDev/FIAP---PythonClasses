
# #Pt.1 - Média aritimética com entrada 3 dados para a média e e saída de dados com a média .
 
num1 = float(input("Digite um número:"))
num2 = float(input("Digite mais número:"))
num3 = float(input("Digite o terceiro e útimo número:"))


#Pt.2 Usuário da um número e dobre na saída de dados.

num4 = float(input("Digite um número:")) #  (input) --> entrada de dados pelo usuário!   

num_dobro = num4 * 2

print("O dobro do número digitado é:", num_dobro)  # (print) --> Sáida de dados para o usuário!


#Pt.3 - Usuário da um número devolve o quadrado do número na saída de dados.

num5 = float(input("Digite um número:")) #  (input) --> entrada de dados pelo usuário!

print("O quadrado do número digitado é:", num5 ** 2)  # (print) --> Sáida de dados para o usuário!


#Pt.4 - Coloque a raiz do valor digitado pelo usuário na saída de dados.

num6 = float(input("Digite um número:")) #  (input) --> entrada de dados pelo usuário!
print("A raiz do número digitado é:", num6 ** 0.5)  # (print) --> Sáida de dados para o usuário!    


#Pt.5 - Conta de baskara com as variáveis a, b e c. O usuário da os valores e o programa devolve as raízes da equação de baskara.
a = float(input("Digite o valor de a:")) #  (input) --> entrada de dados pelo usuário!
b = float(input("Digite o valor de b:")) #  (input) --> entrada de dados pelo usuário!
c = float(input("Digite o valor de c:")) #  (input) --> entrada de dados pelo usuário!

delta = (b ** 2) - (4 * a * c)

rlst = (-b + (delta ** 0.5)) / (2 * a)
rlst2 = (-b - (delta ** 0.5)) / (2 * a)

print("As raízes da equação de baskara são:", rlst, "e", rlst2)  # (print) --> Sáida de dados para o usuário!   


# Pt.6 -Fahrenheit para Celsius. O usuário da a temperatura em Fahrenheit e o programa devolve a temperatura em Celsius.
fahrenheit = float(input("Digite a temperatura em Fahrenheit:")) #  (input) -->
celsius = (fahrenheit - 32) * 5 / 9

kel = celsius + 273.15

print("A temperatura em Celsius é:", celsius)  # (print) --> Sáida de dados para o usuário!
print("A temperatura em Kelvin é:", kel)  # (print) --> Sáida de


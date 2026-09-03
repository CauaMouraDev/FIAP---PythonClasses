# tenho um caixa eletrónico e quero fazer um programa que simule o funcionamento do caixa eletrônico. O usuário vai digitar o valor que deseja sacar e o programa vai devolver a quantidade de notas de cada valor que será entregue ao usuário. As notas disponíveis são: 100, 50, 20, 10, 5, 2 e 1.

num = int(input("Digite o valor que deseja sacar:")) #  (input) --> entrada de dados pelo usuário!

num100 = num // 100
num50 = (num % 100) // 50
num20 = (num % 50) // 20
num10 = (num % 20) // 10
num5 = (num % 10) // 5
num2 = (num % 5) // 2


print("Notas de 100:", num100)
print("Notas de 50:", num50)
print("Notas de 20:", num20)
print("Notas de 10:", num10)
print("Notas de 5:", num5)
print("Notas de 2:", num2)

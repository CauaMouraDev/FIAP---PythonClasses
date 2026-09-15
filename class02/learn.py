#======Formatações=========

#Forma clássica | Exibe tipo de dado | da um espaço entre as informações


nome = "Cauã"

idade = 19
altura = 1.77

print("Nome:",nome , "Idade:", "altura:", altura)
print("\nNome:" ,nome, "\n Idade:", idade, "\nAltura:" ,altura)


# Forma 2 - Realiza concatenação de dados por meio do “ + “ 

# | exibe dados str | da apenas espaço entre as informações;

print("Nome:" + str(nome), "Idade:" + str(idade), "Altura:" +str(altura))
print("Nome:" + str(nome), "\nIdade:" + str(idade), "\nAltura:" +str(altura))

#Forma 3 - Função format() pra a formatação.

print("Nome: {} \nAltura: {} \nIdade: {}" .format(nome,altura,idade))

#Forma 4 - Com uso da forma abreviada do format que é (f "{}")

print(f"nome: {nome} \nidade: {idade} \ne altura = {altura}")
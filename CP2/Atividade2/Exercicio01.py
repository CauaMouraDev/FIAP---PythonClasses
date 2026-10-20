import os
os.system('cls')

senha = ""
defi = input("Defina senha : ")
senha = defi

tent = 0
while tent < 3:
     passw = input("Digite a senha:")
     if passw == senha:
         print("Acesso Permitido!")
         break
     else:
         tent += 1
         rest = 3 - tent
         if rest == 0:
             break
         print(f"restam {rest} tentativas")
         
print("Atingiu o Limite !")

      
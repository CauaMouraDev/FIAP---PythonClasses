quantia = int(input("Digite um valor :")) 

cd50 = quantia // 50
quantia = quantia % 50

cd20 = quantia // 20
quantia = quantia % 20

cd10 = quantia // 10
quantia = quantia % 10

print(cd50, cd20,cd10)

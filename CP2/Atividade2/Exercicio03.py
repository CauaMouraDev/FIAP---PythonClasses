cntA = int(input("Digite o número de alunos da turma: "))
cnt = 0
soma = 0

while cnt < cntA:
    nota = float(input(f"Digite a nota do aluno {cnt + 1}: "))
    soma += nota
    cnt += 1

media = soma / cntA if cntA > 0 else 0
print(f"A média da turma é: {media:.2f}")

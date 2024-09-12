num = int(input("Informe a quantidade de alunos: "))
soma = 0
for x in range (num):
    notas = float(input("Digite a nota do aluno: "))
    soma = soma + notas
media = soma / num
print(media)

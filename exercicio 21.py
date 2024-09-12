n = 1
soma = 0
qtd = int(input("Digite a quantidade de alunos: "))
while n < qtd+1:
    print(f"estamos no passo {qtd} e a soma é {soma}")
    notas = float(input("Informe a nota dos alunos: "))
    soma = soma + notas
    n = n + 1
media = soma / qtd
print(media)

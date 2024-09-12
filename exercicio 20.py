n = 1
soma = 0
while n < 11:
    print(f"estamos no passo {n} e a soma é {soma}")
    nota = float(input("digite uma nota: "))
    soma = soma + nota
    n = n + 1
media = soma / 10
print(media)
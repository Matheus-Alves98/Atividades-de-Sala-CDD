opcao = 1
rep = 0
while opcao != 2 and rep <= 3:
    neg = 0
    for x in range(2):
        num = int(input("Digite um número: "))
        if num < 0:
            neg = neg + 1
    print(neg)
    opcao = int(input("Deseja repetir? 1 sim ou 2 não"))
    rep = rep + 1
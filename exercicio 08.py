n1 = float(input("primeira nota: "))
n2 = float(input("Segunda nota: "))
n3 = float(input("Terceira nota: "))
media =(n1 + n2 + n3) /3
if media >= 7:
    print(f"O aluno esta aprovado com média: {media:.2f} ")
else:
    if media >= 4:
        print(f"O aluno esta em recuperação com média: {media:.2f} ")
    else:
        print(f"O aluno esta reprovado com média: {media:.2f} ")

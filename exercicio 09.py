time1 = input("Digite o nome do time1: ")
time1_gol = int(input("informe os gols do time1: "))
time2 = input("Digite o nome do time2: ")
time2_gol = int(input("informe os gols do time2: "))

if time1_gol == time2_gol:
    print(f"O time jogo entre {time1} x {time2} foi empate")
else:
    if time1_gol > time2_gol:
        print(f"O jogo de {time1} x {time2} teve como vencedor o {time1} com total de {time1_gol} gols")
    else:
        print(f"O jogo entre {time1} x {time2} teve como vencedor {time2} com total de {time2_gol} gols")
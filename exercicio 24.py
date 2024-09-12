n = 1
while n == 1:
    num = int(input("Informe um valor: "))
    while num <= 0:
        num = int(input("Invalido Informe novamente o valor: "))
    for x in range (1,n+1):
         print(x, end = " ")
    n = int(input("deseja colocar outro numero? digite 1 para sim e 2 para não: "))
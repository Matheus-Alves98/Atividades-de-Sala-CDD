h1 = int(input("informe o hora 1: "))
m1 = int(input("Informe o minuto 1: "))
h2 = int(input("informe o hora 2: "))
m2 = int(input("informe o minuto 2: "))
if h1 > 12:
    h1 =h1 -12
if h2 > 12:
    h2 = h2 -12
somahora = h1 + h2
if somahora > 12:
    somahora = somahora -12

somaminutos = m1 + m2

if somaminutos >= 60:
    somaminutos = somaminutos - 60
    somahora = somahora +1

print(f"{somahora}:{somaminutos:02d}")


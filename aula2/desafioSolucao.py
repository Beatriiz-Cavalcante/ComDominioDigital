h1 = int(input("Digite as horas"))
min1 = int(input("Digite os minutos"))
h2 = int(input("Digite as horas"))
min2= int(input("Digite os minutos"))

if h1>12:
    h1 = h1 - 12
if h2>12:
    h2 = h2 -12

hora = h1 + h2

if hora > 12:
    hora= hora - 12

minutos = min1 + min2

if minutos >=60:
    minutos = minutos - 60
    hora = hora + 1

print(f'{hora}:{minutos}')


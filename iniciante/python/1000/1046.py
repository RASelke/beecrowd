entry = input().split()
a = int(entry[0])
b = int(entry[1])

if a > b:
    horas = 24 - a + b
elif b > a:
    horas = b - a
else:
    horas = 24

print(f'O JOGO DUROU {horas} HORA(S)')
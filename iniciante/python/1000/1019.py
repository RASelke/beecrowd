N = int(input())

horas, minutos, segundos = 0,0,0

if N >= 3600:
    horas = N // 3600
    N = N - horas * 3600
if N >= 60:
    minutos = N // 60
    N = N - minutos * 60
if N < 60:
    segundos = N

print(f'{horas}:{minutos}:{segundos}')
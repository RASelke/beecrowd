dia_start = input().split()
hora_start = input().split(sep=' : ')
dia_fim = input().split()
hora_fim = input().split(sep=' : ')

for i in range(3):
    hora_start[i] = int(hora_start[i])
    hora_fim[i] = int(hora_fim[i])

dia_start = int(dia_start[1])
dia_fim = int(dia_fim[1])

if hora_fim[2] >= hora_start[2]:
    segundos = hora_fim[2] - hora_start[2]
else:
    segundos = hora_fim[2] - hora_start[2] + 60
    hora_fim[1] -= 1

if hora_fim[1] >= hora_start[1]:
    minutos = hora_fim[1] - hora_start[1]
else:
    minutos = hora_fim[1] - hora_start[1] + 60
    hora_fim[0] -= 1

if hora_fim[0] >= hora_start[0]:
    horas = hora_fim[0] - hora_start[0]
else:
    horas = hora_fim[0] - hora_start[0] + 24
    dia_fim -= 1

dias = dia_fim - dia_start

print(f'{dias} dia(s)')
print(f'{horas} hora(s)')
print(f'{minutos} minuto(s)')
print(f'{segundos} segundo(s)')
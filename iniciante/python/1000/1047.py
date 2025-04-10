entry = input().strip().split()
inicioHora = int(entry[0])
inicioMinuto = int(entry[1])
finalHora = int(entry[2])
finalMinuto = int(entry[3])

if finalMinuto > inicioMinuto:
    if finalHora > inicioHora:
        totalHora = finalHora - inicioHora
    elif inicioHora > finalHora:
        totalHora = (finalHora - inicioHora) + 24
    else:
        totalHora = 0
    totalMinuto = finalMinuto - inicioMinuto

elif inicioMinuto > finalMinuto:
    if finalHora > inicioHora:
        totalHora = finalHora - inicioHora - 1
    elif inicioHora > finalHora:
        totalHora = finalHora - inicioHora - 1 + 24
    else:
        totalHora = 23
    totalMinuto = (finalMinuto - inicioMinuto) + 60

else:
    if finalHora > inicioHora:
        totalHora = finalHora - inicioHora
    elif inicioHora > finalHora:
        totalHora = finalHora - inicioHora + 24
    else:
        totalHora = 24
    totalMinuto = 0

print(f'O JOGO DUROU {totalHora} HORA(S) E {totalMinuto} MINUTO(S)')
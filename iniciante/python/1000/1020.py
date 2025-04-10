inicial = int(input())

ano, mes, dia = 0,0,0

if inicial >= 365:
    ano = inicial // 365
    inicial = inicial - ano * 365
if inicial >= 30:
    mes = inicial // 30
    inicial = inicial - mes * 30
if inicial < 30:
    dia = inicial

print(f'{ano} ano(s)')
print(f'{mes} mes(es)')
print(f'{dia} dia(s)')
valor = float(input())
valor_inicial = valor

n1, n2, n5, n10, n20, n50, n100 = 0,0,0,0,0,0,0
m1, m50, m25, m10, m05, m01 = 0,0,0,0,0,0

# Notas
if valor >= 100:
    n100 = valor // 100
    valor = valor - n100 * 100
if valor >= 50:
    n50 = valor // 50
    valor = valor - n50 * 50
if valor >= 20:
    n20 = valor // 20
    valor = valor - n20 * 20
if valor >= 10:
    n10 = valor // 10
    valor = valor - n10 * 10
if valor >= 5:
    n5 = valor // 5
    valor = valor - n5 * 5
if valor >= 2:
    n2 = valor // 2
    valor = valor - n2 * 2

print('NOTAS:')
print(f'{int(n100)} nota(s) de R$ 100.00')
print(f'{int(n50)} nota(s) de R$ 50.00')
print(f'{int(n20)} nota(s) de R$ 20.00')
print(f'{int(n10)} nota(s) de R$ 10.00')
print(f'{int(n5)} nota(s) de R$ 5.00')
print(f'{int(n2)} nota(s) de R$ 2.00')

# Moedas
if valor >= 1:
    m1 = valor // 1
    valor = valor - m1 * 1
if valor >= 0.5:
    m50 = valor // 0.5
    valor = valor - m50 * 0.5
if valor >= 0.25:
    m25 = valor // 0.25
    valor = valor - m25 * 0.25
if valor >= 0.1:
    m10 = valor // 0.1
    valor = valor - m10 * 0.1
if valor >= 0.05:
    m05 = valor // 0.05
    valor = valor - m05 * 0.05
m01 = round(valor*100)

print('MOEDAS:')
print(f'{int(m1)} moeda(s) de R$ 1.00')
print(f'{int(m50)} moeda(s) de R$ 0.50')
print(f'{int(m25)} moeda(s) de R$ 0.25')
print(f'{int(m10)} moeda(s) de R$ 0.10')
print(f'{int(m05)} moeda(s) de R$ 0.05')
print(f'{m01} moeda(s) de R$ 0.01')
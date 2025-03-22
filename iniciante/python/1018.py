valor = int(input())
valor_inicial = valor

n1, n2, n5, n10, n20, n50, n100 = 0,0,0,0,0,0,0

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
if valor >= 1:
    n1 = valor // 1
    valor = valor - n1 * 1

print(valor_inicial)
print(f'{n100} nota(s) de R$ 100,00')
print(f'{n50} nota(s) de R$ 50,00')
print(f'{n20} nota(s) de R$ 20,00')
print(f'{n10} nota(s) de R$ 10,00')
print(f'{n5} nota(s) de R$ 5,00')
print(f'{n2} nota(s) de R$ 2,00')
print(f'{n1} nota(s) de R$ 1,00')
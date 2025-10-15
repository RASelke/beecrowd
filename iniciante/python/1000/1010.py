linha1 = input().strip().split()
qt_1 = int(linha1[1])
valor_1 = float(linha1[2])

linha2 = input().strip().split()
qt_2 = int(linha2[1])
valor_2 = float(linha2[2])

VALOR = (qt_1 * valor_1 + qt_2 * valor_2)
print(f'VALOR A PAGAR: R$ {VALOR:.2f}')
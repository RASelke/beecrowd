entry = input().strip().split()
A = float(entry[0])
B = float(entry[1])
C = float(entry[2])

delta = B**2 - 4 * A * C

if A == 0 or delta < 0:
    print("Impossivel calcular")
else:
    x1 = (-B + pow(delta, 1/2)) / (2*A)
    x2 = (-B - pow(delta, 1/2)) / (2*A)
    print(f'R1 = {x1:.5f}')
    print(f'R2 = {x2:.5f}')
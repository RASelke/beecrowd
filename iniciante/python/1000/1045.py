entry = input().split()
for i in range(len(entry)):
    entry[i] = float(entry[i])
entry = sorted(entry, reverse=True)

A = float(entry[0])
B = float(entry[1])
C = float(entry[2])

if A >= (B + C):
    print("NAO FORMA TRIANGULO")

else:
    if (A*A) == (B*B + C*C):
        print("TRIANGULO RETANGULO")

    if (A*A) > (B*B + C*C):
        print("TRIANGULO OBTUSANGULO")

    if (A*A) < (B*B + C*C):
        print("TRIANGULO ACUTANGULO")

    if A == B and B == C:
        print("TRIANGULO EQUILATERO")

    if (A == B or B == C or A == C) and (A != B or B != C):
        print("TRIANGULO ISOSCELES")
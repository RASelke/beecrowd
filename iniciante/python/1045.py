entry = input().strip().split()
entry = sorted(entry, reverse=False)
print(entry)
A = float(entry[0])
B = float(entry[1])
C = float(entry[2])

if A >= B + C:
    print("NAO FORMA TRIANGULO")
if A*A == (B*B + C*C):
    print("TRIANGULO RETANGULO")
if A*A > (B*B + C*C):
    print("TRIANGULO OBSTUSANGULO")
if A*A < (B*B + C*C):
    print("TRIANGULO ACUTANGULO")
if A == B and B == C:
    print("TRIANGULO EQUILATERO")
if (A == B or B == C or A == C) and (A != B and B != C):
    print("TRIANGULO ISOSCELES")
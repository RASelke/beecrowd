entry = input().split()
A = float(entry[0])
B = float(entry[1])
C = float(entry[2])

def verifica_triangulo(A, B, C):
    if A + B > C and B + C > A and A + C > B:
        return True
    else:
        return False
    
if verifica_triangulo(A, B, C) == True:
    print(f"Perimetro = {A + B + C:.1f}")
else:
    area = ((A + B) * C) / 2
    print(f"Area = {area}")
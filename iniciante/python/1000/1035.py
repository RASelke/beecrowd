entry = input().strip().split()
A = int(entry[0])
B = int(entry[1])
C = int(entry[2])
D = int(entry[3])

if B > C and D > A and C+D > A+B and C > 0 and D > 0 and A % 2 == 0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")    
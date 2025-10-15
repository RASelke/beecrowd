x = int(input())
y = int(input())
soma = 0

if x > y:
    soma = x
    x = y
    y = soma
    soma = 0

while x < y-2:
    if x % 2 == 0:
        x += 1
    else:
        x += 2
    soma += x

print(soma)
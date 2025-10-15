pares = 0
for i in range(5):
    entry = int(input())
    if entry % 2 == 0:
        pares += 1

print(f'{pares} valores pares')
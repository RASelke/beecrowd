positivos = []
for i in range(6):
    entry = float(input())
    if entry > 0:
        positivos.append(entry)

print(f'{len(positivos)} valores positivos')
print(f'{sum(positivos) / len(positivos):.1f}')
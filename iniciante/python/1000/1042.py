entry = input().split()
tupla = (int(entry[0]), int(entry[1]), int(entry[2]))

for i in range(len(tupla)):
    print(sorted(tupla)[i])

print("")

for i in range(len(tupla)):
    print(tupla[i])
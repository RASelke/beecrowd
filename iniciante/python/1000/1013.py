entry = input().strip().split()
a = int(entry[0])
b = int(entry[1])
c = int(entry[2])

MaiorAB = int((a+b+abs(a-b)) / 2)

if MaiorAB > c:
    print(f'{MaiorAB} eh o maior')
else:
    print(f'{c} eh o maior')
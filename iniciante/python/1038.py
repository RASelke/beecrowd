entry = input().strip().split()
code = int(entry[0])
qt = int(entry[1])

if code == 1:
    print(f'Total: R$ {qt*4:.2f}')
elif code == 2:
    print(f'Total: R$ {qt*4.5:.2f}')
elif code == 3:
    print(f'Total: R$ {qt*5:.2f}')
elif code == 4:
    print(f'Total: R$ {qt*2:.2f}')
elif code == 5:
    print(f'Total: R$ {qt*1.5:.2f}')
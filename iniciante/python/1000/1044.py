entry = input().split()
A = int(entry[0])
B = int(entry[1])

if A > B:
    if A % B == 0:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')
elif B > A:
    if B % A == 0:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')
else:
    print('Sao Multiplos')
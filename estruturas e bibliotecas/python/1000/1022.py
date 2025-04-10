N = int(input())
X, Y = [], []
resultados = []
saida_simples = []

def MDC(a, b):
    return a if b == 0 else MDC(b, a % b)

for i in range(N):
    entradas = input().strip().split()
    X = int(entradas[0]), entradas[1], int(entradas[2])
    Y = int(entradas[4]), entradas[5], int(entradas[6])
    operador = entradas[3]

    N1, D1, N2, D2 = X[0], X[2], Y[0], Y[2]

    if operador == "+": #SOMA
        resultados.append(N1*D2 + N2*D1)
        resultados.append(D1*D2)
    elif operador == "-": #SUBTRAÇÃO
        resultados.append(N1*D2 - N2*D1)
        resultados.append(D1*D2)
    elif operador == "*": #MULTIPLICAÇÃO
        resultados.append(N1*N2)
        resultados.append(D1*D2)
    elif operador == "/": #DIVISÃO
        resultados.append(N1*D2)
        resultados.append(N2*D1)

    a = resultados[i*2]
    b = resultados[(i*2)+1]

    while True:
        mdc = MDC(a,b)
        if MDC(a, b) == 1:
            saida_simples.append(a)
            saida_simples.append(b)
            break
        else:
            a = a/mdc
            b = b/mdc

for j in range(N):
    print(f'{int(resultados[j*2])}/{int(resultados[(j*2)+1])} = {int(saida_simples[j*2])}/{int(saida_simples[(j*2)+1])}')
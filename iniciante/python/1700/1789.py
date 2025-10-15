while True:
    try:
        L = int(input())
        Vs = input().split()
        for i in range(len(Vs)):
            Vs[i] = float(Vs[i])
        Vs = sorted(Vs, reverse=True)
        if Vs[0] < 10:
            print("1")
        elif Vs[0] >= 10 and Vs[0] < 20:
            print("2")
        elif Vs[0] >= 20:
            print("3")
    except EOFError:
        break
n = int(input())
in_ = 0

for i in range(n):
    x = int(input())
    if x >= 10 and x <= 20:
        in_ += 1

print(f'{in_} in')
print(f'{n - in_} out')
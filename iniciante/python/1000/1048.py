salary = float(input())

if salary >= 0 and salary <= 400:
    new_salary = salary * (1 + 0.15)
elif salary <= 800:
    new_salary = salary * (1 + 0.12)
elif salary <= 1200:
    new_salary = salary * (1 + 0.1)
elif salary <= 2000:
    new_salary = salary * (1 + 0.07)
else:
    new_salary = salary * (1 + 0.04)

print(f'Novo salario: {new_salary:.2f}')
print(f'Reajuste ganho: {new_salary - salary:.2f}')
print(f'Em percentual: {((new_salary - salary) / salary) * 100:.0f} %')
alcool = 0
gasolina = 0
diesel = 0

while True:
    entry = int(input())
    if entry == 4:
        break
    elif entry > 4 and entry < 1:
        continue
    elif entry == 1:
        alcool += 1
    elif entry == 2:
        gasolina += 1
    elif entry == 3:
        diesel += 1

print(f'MUITO OBRIGADO\nAlcool: {alcool}\nGasolina: {gasolina}\nDiesel: {diesel}')
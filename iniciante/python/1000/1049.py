palavra1 = str(input())
palavra2 = str(input())
palavra3 = str(input())

def animal(p2,p3):
    if p2 == 'ave':
        if p3 == 'carnivoro':
            return 'aguia'
        else:
            return 'pomba'
    elif p2 == 'mamifero':
        if p3 == 'onivoro':
            return 'homem'
        else:
            return 'vaca'
    elif p2 == 'inseto':
        if p3 == 'hematofago':
            return 'pulga'
        else:
            return 'lagarta'
    else:
        if p3 == 'hematofago':
            return 'sanguessuga'
        else:
            return 'minhoca'
        
print(animal(palavra2,palavra3))
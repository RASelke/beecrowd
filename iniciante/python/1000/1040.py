entry = input().split()
N1 = float(entry[0])
N2 = float(entry[1])
N3 = float(entry[2])
N4 = float(entry[3])

media = (N1 * 2 + N2 * 3 + N3 * 4 + N4 * 1) / 10

print(f'Media: {media:.1f}')
if media >= 7:
    print("Aluno aprovado.")
elif media < 5:
    print("Aluno reprovado.")
elif media >= 5 and media < 7:
    print("Aluno em exame.")
    nota_exame = float(input())
    print(f"Nota do exame: {nota_exame:.1f}")
    nova_media = (media + nota_exame) / 2
    if nova_media >= 5:
        print("Aluno aprovado.")
    elif nova_media < 5:
        print("Aluno reprovado.")
    print(f"Media final: {nova_media}")
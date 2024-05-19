n1 = float(input('digite a primeira nota: '))
n2 = float(input('digite a segunda nota: '))
media = (n1 + n2)/2
if media <= 5:
    print('Reprovado.')
elif media <= 6.9:
    print('Recuperação.')
elif media >= 7:
    print('Aprovado.')
else:
    print('digite uma nota válida.')
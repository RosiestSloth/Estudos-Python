pessoas = list()
dado = list()
c = 0
sn = ''
maior = 0
menor = 0
m = 0
while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(int(input('Peso: ')))
    dado.append(pessoas[:])
    c += 1
    m += 2
    sn = str(input('Você quer continuar?'))
    pessoas.clear()
    if sn.upper() == 'N':
        break
for i in dado:
    if i[1] >= 90:
        maior += 1
    else:
        menor += 1
print(f'{maior} pessoa(s) possuem maior peso')
print(f'{menor} pessoa(s) possuem menor peso')
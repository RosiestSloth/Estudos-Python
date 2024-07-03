galera = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:]) #O símbolo [:] significa que irá fazer uma cópia e não uma ligação dos dados na lista
    dado.clear()

print(galera)

totmai = 0
totmen = 0

for p in galera:
    if p[1]>= 21:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade')
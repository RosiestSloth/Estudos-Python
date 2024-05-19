matriz = []
p1 = 1
p2 = 1
p3 = 1
for l in range(9):
    matriz.append(int(input(f'Digite o valor para a posição ({p1}, {p2}.): ')))
    p1 +=1
    if p1 == 4:
        p1 -= 3
        p2 += 1
    elif p2 == 4:
        p2 -= 3
        p1 -= 3
        p3 += 1
print('*-' * 4)
print('', matriz[0], matriz[1], matriz[2], '\n',
      matriz[3], matriz[4], matriz[5], '\n',
      matriz[6], matriz[7], matriz[8])
print('*-' * 4)
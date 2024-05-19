matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = 0
for c in range(3):
    for l in range(3):
        matriz[c][l] = int(input(f'Digite o valor da coluna [{c}], [{l}]: '))

print('-='*11)
for o in range(0, 3):
    for c in matriz[o]:
        print(f'[{c:^5}]', end='')
    print()
print('-='*11)

par = list()
dados = list()

while True:
    opcao = str(input('Digite [a] para somar os valores pares\n'
                      '[b] para somar a terceira coluna\n'
                      '[c] para o maior da segunda linha\n'
                      '[d] para sair do programa\n: '))

    if opcao.lower() == 'a':
        for p in range(3):
            for m in range(3):
                if matriz[p][m] % 2 == 0:
                    par.append(matriz[p][m])
        for i in par:
            soma += i
        print(f'A soma dos valores pares {par}, é igual a {soma}.')

    elif opcao.lower() == 'b':
        for k in range(3):
            dados.append(matriz[k][2])
        print(dados)
        for r in dados:
            soma += r
        print(f'A soma dos valores da terceira coluna é {soma}.')

    elif opcao.lower() == 'c':
        maior = matriz[1][:]
        maior.sort()
        print(maior)
        print(f'O maior valor da segunda coluna é {maior[2]}')

    elif opcao.lower() == 'd':
        break

print('Obrigado por utilizar o programa.')

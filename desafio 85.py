print('Você terá que digitar 7 valores.\nPodemos começar? S/N')
r = input()
num = list()
impar = list()
par = list()
n = 1
if r.upper() == 'S':
    for i in range(7):
        num.append(int(input(f'Digite o {n}o valor: ')))
        n +=1
    for ip in num:
        if ip % 2 == 0:
            par.append(ip)
        elif ip % 2 == 1:
            impar.append(ip)
    num.clear()
    num.append(par)
    num.append(impar)
    num.sort(reverse=True)
    print(f'Os valores pares digitados foram {num[0]}.\nE os valores impares foram {num[1]}.')
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
print(f'A soma desses valores é {n1 + n2}')
print(f'A diferênça desses valores é {n1 - n2}')
print(f'A multiplicação desses valores é {n1 * n2}')
print(f'A divisão desses valores é {n1 / n2:.2f}')
if n1 < n2:
    print('O primeiro número é o maior.')
elif n2 < n1:
    print('o segundo valor é o menor.')
else:
    print('Os valores são iguais.')
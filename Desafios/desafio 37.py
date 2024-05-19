num = int(input('Digite um número para conversão: '))
print('digite [1] para binário [2] para octal e [3] para hexadecimal')
opcao = int(input())
if opcao == 1:
    print(f'o número {num} em binário é {bin(num)}')
elif opcao == 2:
    print(f'O número {num} em octal é {oct(num)}')
elif opcao == 3:
    print(f'O número {num} em hexadecimal é {hex(num)}')
else:
    print('digite uma opção válida.')
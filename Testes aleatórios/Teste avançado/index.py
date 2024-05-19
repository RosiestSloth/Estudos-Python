import utilidades
from time import sleep

print('-'*30)
print('          Calculadora')
print('-'*30)

sleep(1.2)

print('Selecione: \n A: Soma: \n B: Subtração: \n C: Multiplicação: \n D: Divisão: \n E: Fatorial: \n S: Sair: ')
print('-'*30)
resp = str(input(': ').upper())
print('-'*30)

while True:
    if resp == 'A':
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))
        res = utilidades.soma(num1, num2)
        print(f'[{num1}] + [{num2}] = [{res}]')
        sleep(1.2)
        print('Selecione: \n A: Soma: \n B: Subtração: \n C: Multiplicação: \n D: Divisão: \n E: Fatorial: \n S: Sair: ')
        print('-'*30)
        resp = str(input(': ').upper())
        print('-'*30)

    elif resp == 'B':
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))
        res = utilidades.sub(num1, num2)
        print(f'[{num1}] - [{num2}] = [{res}]')
        sleep(1.2)
        print('Selecione: \n A: Soma: \n B: Subtração: \n C: Multiplicação: \n D: Divisão: \n E: Fatorial: \n S: Sair: ')
        print('-'*30)
        resp = str(input(': ').upper())
        print('-'*30)

    elif resp == 'C':
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))
        res = utilidades.mult(num1, num2)
        print(f'[{num1}] X [{num2}] = [{res}]')
        sleep(1.2)
        print('Selecione: \n A: Soma: \n B: Subtração: \n C: Multiplicação: \n D: Divisão: \n E: Fatorial: \n S: Sair: ')
        print('-'*30)
        resp = str(input(': ').upper())
        print('-'*30)

    elif resp == 'D':
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))
        res = utilidades.div(num1, num2)
        print(f'[{num1}] ÷ [{num2}] = [{res}]')
        sleep(1.2)
        print('Selecione: \n A: Soma: \n B: Subtração: \n C: Multiplicação: \n D: Divisão: \n E: Fatorial: \n S: Sair: ')
        print('-'*30)
        resp = str(input(': ').upper())
        print('-'*30)

    elif resp == 'E':
        num1 = int(input('Digite o número: '))
        res = utilidades.fat(num1)
        print(f'[{num1}!] = [{res}]')
        sleep(1.2)
        print('Selecione: \n A: Soma: \n B: Subtração: \n C: Multiplicação: \n D: Divisão: \n E: Fatorial: \n S: Sair: ')
        print('-'*30)
        resp = str(input(': ').upper())
        print('-'*30)

    elif resp == 'S':
        print('Encerrando')
        sleep(1)
        break

print('-'*30)
print('Obrigado por utilizar')
print('-'*30)
